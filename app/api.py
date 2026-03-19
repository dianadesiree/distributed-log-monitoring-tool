"""
REST API for the Log Monitoring Tool
Exposes endpoints to receive and query logs
"""

from flask import Flask, request, jsonify
from .collector import LogCollector
import logging
import os

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize Flask app and collector
app = Flask(__name__)
collector = LogCollector()

@app.route('/api/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({'status': 'healthy', 'service': 'log-monitor'})

@app.route('/api/logs', methods=['POST'])
def receive_log():
    """
    Endpoint to receive new logs
    Expected JSON format:
    {
        "level": "ERROR|WARNING|INFO|DEBUG",
        "message": "log message",
        "source": "application name",
        "context": {}  # optional additional data
    }
    """
    try:
        log_data = request.get_json()
        
        if not log_data:
            return jsonify({'error': 'No JSON data provided'}), 400
        
        if 'message' not in log_data:
            return jsonify({'error': 'Missing required field: message'}), 400
        
        # Add source if not provided
        if 'source' not in log_data:
            log_data['source'] = 'unknown'
        
        # Collect the log
        success = collector.collect_log(log_data)
        
        if success:
            return jsonify({'status': 'logged'}), 201
        else:
            return jsonify({'error': 'Failed to store log'}), 500
            
    except Exception as e:
        logger.error(f"Error processing log: {str(e)}")
        return jsonify({'error': str(e)}), 500

@app.route('/api/logs', methods=['GET'])
def get_logs():
    """Retrieve logs with optional filters"""
    date = request.args.get('date')
    level = request.args.get('level')
    limit = request.args.get('limit', 100, type=int)
    
    logs = collector.get_logs(date=date, level=level, limit=limit)
    return jsonify({'logs': logs, 'count': len(logs)})

@app.route('/api/metrics', methods=['GET'])
def get_metrics():
    """Get metrics summary"""
    metrics = collector.get_metrics()
    return jsonify(metrics)

@app.route('/api/logs/<path:date>', methods=['DELETE'])
def delete_logs(date):
    """
    Delete logs for a specific date
    """
    try:
        import os
        from pathlib import Path
        
        log_file = Path('logs') / f"logs_{date}.json"
        if log_file.exists():
            os.remove(log_file)
            return jsonify({'status': f'Deleted logs for {date}'})
        else:
            return jsonify({'error': 'No logs found for this date'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)