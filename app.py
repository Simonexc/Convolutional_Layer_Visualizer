import os
from werkzeug.utils import secure_filename
from flask import Flask, request, render_template, send_from_directory


app = Flask(__name__)
APP_ROOT = os.path.dirname(os.path.abspath(__file__))


@app.route("/", methods=["POST", "GET"])
def home_func():
    if request.method == 'POST':
        # all images will be uploaded to 'uploads' folder
        target = os.path.join(APP_ROOT, 'uploads/')

        # create image directory if not found
        if not os.path.isdir(target):
            os.mkdir(target)

        upload = request.files.getlist("file")[0]

        # save image
        filename = secure_filename(upload.filename)
        destination = "/".join([target, filename])
        upload.save(destination)

        return render_template("home.html", image_name=filename)

    else:

        return render_template("home.html", image_name=None)


@app.route('/uploads/<filename>')
def send_image(filename):
    return send_from_directory("uploads", filename)


if __name__ == "__main__":
    app.run()