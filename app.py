from flask import Flask, request, jsonify
import datetime

app = Flask(__name__)

@app.route('/endpoint', methods=['GET'])
def get_info():
    # Get query parameters
    slack_name = request.args.get('slack_name')
    track = request.args.get('track')

    # Get current day and UTC time
    current_day = datetime.datetime.utcnow().strftime("%A")
    utc_time = datetime.datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")

    # Validate UTC time +/- 2 hours
    current_utc_time = datetime.datetime.strptime(utc_time, "%Y-%m-%dT%H:%M:%SZ")
    valid_time_range = datetime.timedelta(hours=2)
    utc_now = datetime.datetime.utcnow()
    if utc_now - valid_time_range <= current_utc_time <= utc_now + valid_time_range:
        is_valid_utc = True
    else:
        is_valid_utc = False

    # Get GitHub URLs
    github_file_url = "https://github.com/username/repo/blob/main/file_name.ext"
    github_repo_url = "https://github.com/akinbabs54/hng_backend"

    response = {
        "slack_name": slack_name,
        "current_day": current_day,
        "utc_time": utc_time,
        "track": track,
        "github_file_url": github_file_url,
        "github_repo_url": github_repo_url,
        "status_code": 200 if is_valid_utc else 400
    }

    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)