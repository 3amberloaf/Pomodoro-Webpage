from flask import Blueprint, render_template, jsonify
from flask_login import login_required

pomodoro = Blueprint('pomodoro', __name__, template_folder='templates')


@pomodoro.route('/start_timer', methods=['POST'])
@login_required
def start_timer():
    """Start the Pomodoro timer."""
    # Business logic for starting the timer
    return jsonify(message="Timer started"), 204


@pomodoro.route('/stop_timer', methods=['POST'])
@login_required
def stop_timer():
    """Stop the Pomodoro timer."""
    # Business logic for stopping the timer
    return jsonify(message="Timer stopped"), 204


@pomodoro.route('/update_timer_display', methods=['POST'])
@login_required
def update_timer_display():
    """Update the Pomodoro timer display."""
    # Business logic for updating the timer display
    return jsonify(timer_display="00:00"), 200


@pomodoro.route('/render_pomodoro_page', methods=['GET'])
@login_required
def render_pomodoro_page():
    """Render the Pomodoro page."""
    return render_template('templates/Pomodoro.html')
