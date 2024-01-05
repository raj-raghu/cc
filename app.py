from flask import Flask, render_template, request, jsonify
import pymysql

app = Flask(__name__)

# Replace these with your MySQL database details
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'G1e1919#',
    'database': 'flask',
}

# Function to execute MySQL queries
def execute_query(query, fetch=True):
    connection = pymysql.connect(**db_config)
    cursor = connection.cursor()
    cursor.execute(query)
    if fetch:
        result = cursor.fetchall()
    else:
        result = None
    connection.commit()
    connection.close()
    return result

@app.route('/')
def index():
    query = "SELECT * FROM xilinx_31_12"
    data = execute_query(query)

    # Fetch column names dynamically from the database
    cursor = pymysql.connect(**db_config).cursor()
    cursor.execute(f"SHOW COLUMNS FROM xilinx_31_12")
    columns = [column[0] for column in cursor.fetchall()]

    return render_template('index.html', columns=columns, data=data)

@app.route('/update_data', methods=['POST'])
def update_data():
    role_id = request.form.get('RoleID')
    role_name = request.form.get('RoleName')
    url = request.form.get('URL')
    company = request.form.get('Company')
    location = request.form.get('Location')
    department = request.form.get('Department')
    teams = request.form.get('Teams')
    eligibility = request.form.get('Eligibility')
    all_text = request.form.get('AllText')
    date = request.form.get('PostedDate')
    sdv = request.form.get('isSDV')

    # Additional empty columns
    domain = request.form.get('Domain', '')
    subdomain = request.form.get('SubDomain', '')

    # Update query with the new columns
    query = f"UPDATE xilinx_31_12 SET RoleName='{role_name}', URL='{url}', Company='{company}', " \
            f"Location='{location}', Department='{department}', Teams='{teams}', " \
            f"Eligibility='{eligibility}', AllText='{all_text}', PostedDate='{date}', isSDV='{sdv}', " \
            f"Domain='{domain}', SubDomain='{subdomain}' " \
            f"WHERE RoleID='{role_id}'"

    execute_query(query, fetch=False)

    return jsonify({'success': True})

if __name__ == '__main__':
    app.run(debug=True)
