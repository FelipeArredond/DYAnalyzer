# import docker

# client = docker.from_env()

def downloadTrivyImage():
    # client.images.pull("bitnami/trivy") #The program needs to pull the official docker image
    # Container = client.containers.create('bitnami/trivy') # We create a new Container using the trivy image
    # Container.start()
    # container_result = str(client.containers.list()[0])
    # container_id = container_result[12:len(container_result)-1]
    # result_container = client.containers.run('bitnami/trivy', "image python:3.9-alpine", detach=True)
    # scan_logs = []
    # for line in result_container.logs(stream=True):
    #     scan_logs.append(line.strip())
    # return scan_logs
    return 'Logs from con'
