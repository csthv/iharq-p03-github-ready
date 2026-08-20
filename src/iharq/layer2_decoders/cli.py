import argparse,json
from .kaggle_entry import authoring_fixture_simulation
def main():
 p=argparse.ArgumentParser();p.add_argument('--package-root',default='.');p.add_argument('--work-root',default='./fixture_work');p.add_argument('--fixture-simulation',action='store_true');a=p.parse_args()
 if a.fixture_simulation:print(json.dumps(authoring_fixture_simulation(a.package_root,a.work_root),indent=2,default=str))
if __name__=='__main__':main()
