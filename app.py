from flask import Flask, request, jsonify, make_response
from concurrent.futures import ThreadPoolExecutor
from utils.Search import Search

app = Flask(__name__)
executor = ThreadPoolExecutor(max_workers=10)

@app.route("/api/v1/search", methods=["GET"])
def search():
    query = request.args.get('query')

    if query:
        future = executor.submit(service_request, query)
        return future.result()
    else:
        return make_response(jsonify({'Status': 422, 'Error': 'Unprocessable Entity'}), 422)

@app.route("/api/v1/metrics", methods=["GET"])
def metrics():
    return service_request("Netrin, a melhor empresa")


def service_request(query) -> str:
    src = Search(query)
    return src.search() 


if __name__ == '__main__':
    app.run(debug=False, host="0.0.0.0")
