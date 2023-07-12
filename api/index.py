from flask import Flask, request, jsonify
from modules.solver import (
    TeachingSolver,
)  # assuming you've moved the code into a separate file

from dataclasses import dataclass
from typing import List

app = Flask(__name__)


@dataclass
class Person:
    name: str
    out: List[str]


@dataclass
class TeachingData:
    data: List[Person]
    n_blocks: int
    weights: List[float]
    low_priority_weight: float
    exclude_presenters: List[str]
    first_time_people: List[str]


@app.route("/solve", methods=["POST"])
def solve_teaching_problem():
    data = request.get_json()
    data.setdefault("weights", [1, 2, 3, 4])
    data.setdefault("low_priority_weight", 10)
    data.setdefault("n_blocks", 2)
    data.setdefault("exclude_presenters", [])
    data.setdefault("first_time_people", [])
    teaching_data = TeachingData(**data)

    # Create solver and solve problem
    solver = TeachingSolver(
        teaching_data.data,
        teaching_data.n_blocks,
        teaching_data.weights,
        teaching_data.low_priority_weight,
        teaching_data.exclude_presenters,
        teaching_data.first_time_people,
    )
    solver.solve(print_status=False, print_cost_achieved=False)

    results = solver.get_results()

    # Return results as JSON
    return jsonify(results), 200


if __name__ == "__main__":
    app.run(debug=False)
