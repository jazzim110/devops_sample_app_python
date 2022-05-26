from flask import Flask, jsonify, request
from prometheus_flask_exporter import PrometheusMetrics
from random import randrange
import time


def create_app():
  app = Flask(__name__)

  @app.route("/healthz")
  def healthz():
    return {
      "status": 200,
      "message": "healthy"
    }

  @app.route("/hello")
  def hello():
    return jsonify({"message": "Hello world !!\n"}), 200

  @app.route("/hello/<username>")
  def hello_user(username):
    return jsonify({"message": "Hello %s\n" % username}), 200

  return app


if __name__ == "__main__":
  app = create_app()
  app.run(host='0.0.0.0')
