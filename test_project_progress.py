from project_progress import process_project_data

def test_default_project_values():
    result = process_project_data(["project_progress.py"])

    assert result["project_id"] == "PRJ101"
    assert result["project_name"] == "Project Tracker"
    assert result["month"] == "January"
    assert result["tasks"] == [18, 15, 17]
    assert result["total"] == 50
    assert result["average"] == (50 / 3)
    assert result["progress"] == "Good Progress"


def test_command_line_project_arguments():
    args = [
        "project_progress.py",
        "PRJ205",
        "CI_CD_System",
        "March",
        "20",
        "18",
        "22"
    ]

    result = process_project_data(args)

    assert result["project_id"] == "PRJ205"
    assert result["project_name"] == "CI_CD_System"
    assert result["month"] == "March"
    assert result["tasks"] == [20, 18, 22]
    assert result["total"] == 60
    assert result["average"] == 20
    assert result["progress"] == "Excellent Progress"