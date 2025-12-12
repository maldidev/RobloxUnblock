# IF YOU HAVE THOUGH THAT IS WILL RUIN YOUR COMPUTER THEN EDIT IT.
# THIS FILE IS NOT SAFE FOR USING AS NOT PROFFESIONAL!
import os
import sys
import random
import json
import platform
import subprocess
from datetime import datetime
from pathlib import Path

class RegionManager:
    def __init__(self):
        self.system = platform.system()
        self.backup_file = Path.home() / 'region_backup.json'
        
    def get_regions(self):
        if self.system == 'Windows':
            return [
                {'name': 'Russia', 'tz': 'Russian Standard Time', 'geo': 'RU'},
                {'name': 'USA', 'tz': 'Eastern Standard Time', 'geo': 'US'},
                {'name': 'UK', 'tz': 'GMT Standard Time', 'geo': 'GB'},
                {'name': 'Germany', 'tz': 'W. Europe Standard Time', 'geo': 'DE'},
                {'name': 'Japan', 'tz': 'Tokyo Standard Time', 'geo': 'JP'},
                {'name': 'Australia', 'tz': 'AUS Eastern Standard Time', 'geo': 'AU'},
                {'name': 'UAE', 'tz': 'Arabian Standard Time', 'geo': 'AE'},
                {'name': 'India', 'tz': 'India Standard Time', 'geo': 'IN'},
                {'name': 'Brazil', 'tz': 'E. South America Standard Time', 'geo': 'BR'},
                {'name': 'China', 'tz': 'China Standard Time', 'geo': 'CN'}
            ]
        else:
            return [
                {'name': 'Russia', 'tz': 'Europe/Moscow', 'geo': 'RU'},
                {'name': 'USA', 'tz': 'America/New_York', 'geo': 'US'},
                {'name': 'UK', 'tz': 'Europe/London', 'geo': 'GB'},
                {'name': 'Germany', 'tz': 'Europe/Berlin', 'geo': 'DE'},
                {'name': 'Japan', 'tz': 'Asia/Tokyo', 'geo': 'JP'},
                {'name': 'Australia', 'tz': 'Australia/Sydney', 'geo': 'AU'},
                {'name': 'UAE', 'tz': 'Asia/Dubai', 'geo': 'AE'},
                {'name': 'India', 'tz': 'Asia/Kolkata', 'geo': 'IN'},
                {'name': 'Brazil', 'tz': 'America/Sao_Paulo', 'geo': 'BR'},
                {'name': 'China', 'tz': 'Asia/Shanghai', 'geo': 'CN'}
            ]
    
    def backup_current(self):
        backup = {'system': self.system}
        
        if self.system == 'Windows':
            try:
                result = subprocess.run(['powershell', '-Command', 'Get-TimeZone'], 
                                      capture_output=True, text=True, shell=True)
                backup['timezone'] = result.stdout.strip()
                
                result = subprocess.run(['reg', 'query', 'HKLM\\SYSTEM\\CurrentControlSet\\Control\\Nls\\Geo', '/v', 'Nation'],
                                      capture_output=True, text=True, shell=True)
                lines = result.stdout.split('\n')
                for line in lines:
                    if 'Nation' in line:
                        backup['geo'] = line.split()[-1]
                        break
            except:
                pass
                
        else:
            try:
                result = subprocess.run(['timedatectl', 'show', '--property=Timezone', '--value'], 
                                      capture_output=True, text=True)
                backup['timezone'] = result.stdout.strip()
                
                result = subprocess.run(['cat', '/etc/timezone'], 
                                      capture_output=True, text=True)
                if result.returncode == 0:
                    backup['geo_tz'] = result.stdout.strip()
            except:
                pass
        
        with open(self.backup_file, 'w') as f:
            json.dump(backup, f)
        return True
    
    def apply_random(self):
        regions = self.get_regions()
        region = random.choice(regions)
        
        print(f"Setting region to: {region['name']}")
        self.backup_current()
        
        if self.system == 'Windows':
            subprocess.run(['powershell', '-Command', f'Set-TimeZone -Id "{region["tz"]}"'], 
                         shell=True)
            subprocess.run(['reg', 'add', 'HKLM\\SYSTEM\\CurrentControlSet\\Control\\Nls\\Geo', 
                          '/v', 'Nation', '/t', 'REG_DWORD', '/d', str(self._country_to_code(region['geo'])), 
                          '/f'], shell=True)
            
        else:
            subprocess.run(['sudo', 'timedatectl', 'set-timezone', region['tz']])
            subprocess.run(['sudo', 'ln', '-sf', f'/usr/share/zoneinfo/{region["tz"]}', '/etc/localtime'])
        
        print(f"Timezone: {region['tz']}")
        print(f"Geo location: {region['geo']}")
        return region
    
    def _country_to_code(self, country):
        codes = {
            'RU': 7, 'US': 244, 'GB': 242, 'DE': 94, 
            'JP': 122, 'AU': 12, 'AE': 784, 'IN': 113,
            'BR': 76, 'CN': 86
        }
        return codes.get(country, 244)
    
    def restore(self):
        if not os.path.exists(self.backup_file):
            print("No backup found")
            return False
        
        with open(self.backup_file, 'r') as f:
            backup = json.load(f)
        
        print("Restoring original settings...")
        
        if self.system == 'Windows':
            if 'timezone' in backup:
                subprocess.run(['powershell', '-Command', f'Set-TimeZone -Id "{backup["timezone"]}"'], 
                             shell=True)
            if 'geo' in backup:
                subprocess.run(['reg', 'add', 'HKLM\\SYSTEM\\CurrentControlSet\\Control\\Nls\\Geo', 
                              '/v', 'Nation', '/t', 'REG_DWORD', '/d', backup['geo'], 
                              '/f'], shell=True)
                
        else:
            if 'timezone' in backup:
                subprocess.run(['sudo', 'timedatectl', 'set-timezone', backup['timezone']])
            if 'geo_tz' in backup:
                subprocess.run(['sudo', 'ln', '-sf', f'/usr/share/zoneinfo/{backup["geo_tz"]}', '/etc/localtime'])
        
        os.remove(self.backup_file)
        print("Restore complete")
        return True
    
    def show_current(self):
        print(f"System: {self.system}")
        
        if self.system == 'Windows':
            result = subprocess.run(['powershell', '-Command', 'Get-TimeZone'], 
                                  capture_output=True, text=True, shell=True)
            print(f"Timezone: {result.stdout.strip()}")
            
            result = subprocess.run(['reg', 'query', 'HKLM\\SYSTEM\\CurrentControlSet\\Control\\Nls\\Geo', 
                                   '/v', 'Nation'], capture_output=True, text=True, shell=True)
            print(f"Geo location code: {result.stdout.split()[-1] if 'Nation' in result.stdout else 'Unknown'}")
            
        else:
            result = subprocess.run(['timedatectl', 'status'], capture_output=True, text=True)
            print(result.stdout)
            
            if os.path.exists('/etc/timezone'):
                result = subprocess.run(['cat', '/etc/timezone'], capture_output=True, text=True)
                print(f"Timezone file: {result.stdout.strip()}")

def main():
    if len(sys.argv) < 2:
        print("Usage: python region_manager.py [set|restore|status]")
        return
    
    manager = RegionManager()
    
    if sys.argv[1] == 'set':
        manager.apply_random()
    elif sys.argv[1] == 'restore':
        manager.restore()
    elif sys.argv[1] == 'status':
        manager.show_current()
    else:
        print("Unknown command. Use: set, restore, status")

if __name__ == '__main__':
    main()
