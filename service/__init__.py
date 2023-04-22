import importlib
import os


def load_services(service_dir, service_filter: lambda service: any):
    return service_filter(in_load_services(service_dir))


def in_load_services(service_dir):
    """Load all services in the service directory."""
    services = []

    for service in os.listdir(service_dir):
        if service.endswith(".py") and service != "__init__.py":
            services.append(load_service(service_dir, service))
    return services


def load_service(service_dir, service):
    """Load a single service."""
    service_name = service[:-3]
    service_module = importlib.import_module(service_dir + "." + service_name)
    return service_module
