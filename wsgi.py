#"app" and host need to be changed
from main import app 
 
if __name__ == "__main__":
    # runs the application on the repl development server
    app.run(debug=True, host='192.168.1.1', port='3000'
