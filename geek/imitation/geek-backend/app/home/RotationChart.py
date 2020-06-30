from app.home import home_api
from settings import GEEK_DB

@home_api.route('/get_rotation_chart')
def get_rotation_chart():

    sql = 'select '

    GEEK_DB.cursor.execute()