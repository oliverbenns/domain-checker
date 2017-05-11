# Domain Checker
Tool to check if domains are available - notifies with Mac notifications.

## Dependencies

- Python 3
- Bash + Whois + Grep (probably already installed)

## Usage

- Edit `config.py` to include domain names and extensions that you want to check.
- Run `./domain-checker.py`

## Automatic checking

- Set up a Cronjob:
  - `export VISUAL=nano; crontab -e` (or use Vim if you want).
  - Add `0 */6 * * * /path/to/domain-checker.py` (run every 6 hours - change this if you want).
