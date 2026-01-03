def main():
    spacecraft = {"name": "Voyager 1", "distance" : "163 AU"}
    print(create_report(spacecraft))
    
def create_report(spacecraft):
    report = f"""
    ======REPORT======
    Name : {spacecraft['name']}
    Distance : {spacecraft['distance']}
    ==================
    """
    return report
main()  