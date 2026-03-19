"""
Log Collector Module
Responsible for receiving and storing log entries
"""

import json
import logging
from datetime import datetime
from pathlib import Path

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class LogCollector:
    """Collects and stores log entries from various sources"""
    
    def __init__(self, log_directory="logs"):
        self.log_directory = Path(log_directory)
        self.log_directory.mkdir(exist_ok=True)
        logger.info(f"Log collector initialized. Storing logs in {self.log_directory}")
    
    def collect_log(self, log_data):
        """
        Collect and store a single log entry
        
        Args:
            log_data (dict): Log entry with timestamp, level, message, etc.
        
        Returns:
            bool: True if successful, False otherwise
        """
        try:
            # Add received timestamp if not present
            if 'timestamp' not in log_data:
                log_data['timestamp'] = datetime.now().isoformat()
            
            # Determine log file based on date
            today = datetime.now().strftime('%Y-%m-%d')
            log_file = self.log_directory / f"logs_{today}.json"
            
            # Append log to file
            with open(log_file, 'a', encoding='utf-8') as f:
                f.write(json.dumps(log_data) + '\n')
            
            logger.info(f"Log collected: {log_data.get('level', 'INFO')} - {log_data.get('message', '')[:50]}")
            return True
            
        except Exception as e:
            logger.error(f"Failed to collect log: {str(e)}")
            return False
    
    def get_logs(self, date=None, level=None, limit=100):
        """
        Retrieve logs with optional filtering
        
        Args:
            date (str, optional): Date in YYYY-MM-DD format
            level (str, optional): Filter by log level
            limit (int): Maximum number of logs to return
        
        Returns:
            list: Matching log entries
        """
        if date is None:
            date = datetime.now().strftime('%Y-%m-%d')
        
        log_file = self.log_directory / f"logs_{date}.json"
        logs = []
        
        if log_file.exists():
            with open(log_file, 'r', encoding='utf-8') as f:
                for i, line in enumerate(f):
                    if i >= limit:
                        break
                    try:
                        log = json.loads(line.strip())
                        if level is None or log.get('level') == level:
                            logs.append(log)
                    except json.JSONDecodeError:
                        continue
        
        return logs
    
    def get_metrics(self):
        """
        Generate simple metrics from collected logs
        
        Returns:
            dict: Metrics summary
        """
        metrics = {
            'total_logs': 0,
            'by_level': {'ERROR': 0, 'WARNING': 0, 'INFO': 0, 'DEBUG': 0},
            'recent_errors': []
        }
        
        # Get today's logs
        today = datetime.now().strftime('%Y-%m-%d')
        logs = self.get_logs(today, limit=1000)
        
        for log in logs:
            metrics['total_logs'] += 1
            level = log.get('level', 'INFO')
            if level in metrics['by_level']:
                metrics['by_level'][level] += 1
            
            if level == 'ERROR' and len(metrics['recent_errors']) < 10:
                metrics['recent_errors'].append({
                    'time': log.get('timestamp'),
                    'message': log.get('message', '')
                })
        
        return metrics