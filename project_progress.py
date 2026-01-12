import sys

def process_project_data(argv=None):
    if argv is None:
        argv = sys.argv

    # Check command-line arguments
    if len(argv) == 7:
        script_name = argv[0]
        project_id = argv[1]
        project_name = argv[2]
        sprint_month = argv[3]
        p1 = argv[4]   # Tasks in Phase 1
        p2 = argv[5]   # Tasks in Phase 2
        p3 = argv[6]   # Tasks in Phase 3
    else:
        script_name = argv[0]
        project_id = "PRJ101"
        project_name = "Project Tracker"
        sprint_month = "January"
        p1 = "18"
        p2 = "15"
        p3 = "17"

    # Convert task counts to integers
    tasks = [int(p1), int(p2), int(p3)]

    # Calculate total and average
    total_tasks = sum(tasks)
    average_tasks = total_tasks / len(tasks)

    # Project progress analysis
    if average_tasks >= 15:
        progress_level = "Excellent Progress"
    elif average_tasks >= 10:
        progress_level = "Good Progress"
    elif average_tasks >= 7:
        progress_level = "Moderate Progress"
    else:
        progress_level = "Poor Progress"

    return {
        "script_name": script_name,
        "project_id": project_id,
        "project_name": project_name,
        "month": sprint_month,
        "tasks": tasks,
        "total": total_tasks,
        "average": average_tasks,
        "progress": progress_level
    }

if __name__ == "__main__":
    result = process_project_data()

    print("Script Name:", result["script_name"])
    print("Project ID:", result["project_id"])
    print("Project Name:", result["project_name"])
    print("Sprint Month:", result["month"])
    print("Tasks Completed (Phases):", *result["tasks"])
    print("Total Tasks Completed:", result["total"])
    print("Average Tasks per Phase:", result["average"])
    print("Project Progress Level:", result["progress"])