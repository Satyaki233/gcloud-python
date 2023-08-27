import createInstance
import deleteInstance
import showInstance
import uuid
import google.auth
import google.auth.exceptions

def createGcpInstance():
    try:
        default_project_id = google.auth.default()[1]
    except google.auth.exceptions.DefaultCredentialsError:
        print(
            "Please use `gcloud auth application-default login` "
            "or set GOOGLE_APPLICATION_CREDENTIALS to use this script."
        )
    else:
        instance_name = str(input("Enter the name of Instance  : "))
        instance_zone = str(input("Enter the name of the zone : "))

        publicImages = [
            {
                "NAME": "ubuntu-minimal-2004-focal-v20230818",
                "PROJECT": "ubuntu-os-cloud",
                "FAMILY": "ubuntu-2004-lts",
            },
            {
                "NAME": "debian-11-bullseye-v20230306",
                "PROJECT": "debian-cloud",
                "FAMILY": "debian-11",
            }
        ]

        print("The list of os : ")
        for i in publicImages:
            print(i , i.get("NAME"))

        choosenOs = int(input("Enter 1 o 2 chose between two : "))
        cloud_project ="",
        cloud_family =""

        if(choosenOs == 1):
            cloud_project= publicImages[0].get("PROJECT")
            cloud_family= publicImages[0].get("FAMILY")
        else:
            cloud_project= publicImages[1].get("PROJECT")
            cloud_family= publicImages[1].get("FAMILY")
        
        storage = int(input("Enter the amount of storage : "))

        newest_debian = createInstance.get_image_from_family(
            project=cloud_project, family=cloud_family
        )
        disk_type = f"zones/{instance_zone}/diskTypes/pd-standard"
        disks = [createInstance.disk_from_image(disk_type, storage, True, newest_debian.self_link)]

        createInstance.create_instance(default_project_id, instance_zone, instance_name, disks,machine_type="e2-standard-4")


def showGcpInstances():
    project_id = google.auth.default()[1]
    zone = str(input("Enter zone : "))

    showInstance.list_instances(project_id, zone)

def delGcpInstance():
    project_id = google.auth.default()[1]
    zone = str(input("Enter zone : "))
    machine_name= str(input("Enter the name of the instance(instance-id) : "))
    deleteInstance.delete_instance(project_id, zone, machine_name)

if __name__ == "__main__":
    n=1
    while(n>0):
        if(n==1):
            print("\t\n----------GCP----------\n")
            print("""
            \n\t
            [1].Menu\n\t
            [2].Create Instance\n\t
            [3].Show Instance\n\t
            [4].Delete Instance\n\t
            [0].Exit\n\t
                """)
            n=int(input("Enter a number for desird action: "))
        elif(n==2):
            createGcpInstance()
            n=1
        elif(n==3):
            showGcpInstances()
            n=1
        elif(n==4):
            delGcpInstance()
            n=1
        else:
            print("\t\nEnter a valid input\nEnter 0 to exit")
            n=1

    print("\n------Thank you ------")

