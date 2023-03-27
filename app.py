from flask import Flask, render_template, request

app = Flask(__name__)

# Define a Flask route to handle GET requests to the root URL and URLs with a specified file name.
@app.route('/')
@app.route('/<filename>')
def show_file(filename='file1.txt'):
    # Get the values of the 'start' and 'end' parameters from the query string.
    start_line = request.args.get('start')
    end_line = request.args.get('end')

    try:
        # Open the specified file for reading.
        with open(filename, 'r') as f:
            # Read all lines from the file into a list.
            lines = f.readlines()

            # If both the 'start' and 'end' parameters are present, slice the list of lines to include only the specified range.
            if start_line and end_line:
                start_line = int(start_line)
                end_line = int(end_line)
                lines = lines[start_line-1:end_line]

            # Render the 'file.html' template with the list of lines and the file name.
            return render_template('file.html', lines=lines, filename=filename)

    # Catch any exceptions that might be raised if the file cannot be found or the parameters are invalid.
    except (FileNotFoundError, ValueError):
        # Render the 'error.html' template with a message indicating that the file was not found or the parameters are invalid.
        return render_template('error.html', message='File not found or invalid input')

# Run the Flask application if this module is being executed as the main program.
if __name__ == '__main__':
    app.run(debug=True)
