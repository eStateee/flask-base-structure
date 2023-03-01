from app import create_app

# If you don't want to run application through console.
# You can just run this file with all necessary settings you need


# Get app from Application Factory
app = create_app()

if __name__ == '__main__':
    app.run(debug=True, port=5000)
