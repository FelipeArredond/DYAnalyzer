import syft

def analyze_container_image(image_name):
    # Load the Docker image
    image = syft.DockerImage(image_name)
    
    # Perform image analysis
    analysis = image.analysis()
    
    return analysis

def analyze_yaml_file(yaml_file_path):
    # Load the Kubernetes YAML file
    kube_config = syft.KubeConfig(yaml_file_path)
    
    # Perform analysis of Kubernetes resources
    analysis = kube_config.analysis()
    
    return analysis

def main():
    image_name = 'ubuntu:latest'  # Replace with your image name
    yaml_file_path = 'path/to/your/kubernetes.yaml'  # Replace with your YAML file path
    
    image_analysis = analyze_container_image(image_name)
    yaml_analysis = analyze_yaml_file(yaml_file_path)
    
    print("Container Image Analysis:")
    print(image_analysis)
    
    print("\nYAML File Analysis:")
    print(yaml_analysis)

if __name__ == "__main__":
    main()
