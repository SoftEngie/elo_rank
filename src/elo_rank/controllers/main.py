from flask import Blueprint, render_template

from elo_rank.models.users import User
from elo_rank import assets_folder
main = Blueprint("main", __name__)


@main.route("/")
def index():
    return render_template("index.html")


@main.route('/rules')
def rules():
    return render_template('rules.html')


@main.route('/leaderboard')
def leaderboard():
    users_data = User.query.with_entities(User.email, User.score).all()
    users = sorted([{'email': user.email, 'score': user.score} for user in users_data],
                   reverse=True, key=lambda user: user['score'])
    return render_template('leaderboard.html', top_users=users[3:],
                           other_users=users[:3],
                           gold_cup_asset=assets_folder/"gold_cup.svg",
                           silver_medal_asset=assets_folder/"silver_medal.svg",
                           bronze_medal_asset=assets_folder/"bronze_medal.svg"
                           )
