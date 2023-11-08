class Project:
    def __init__(self, name, description, dependencies, dev_dependencies, license, authors):
        self.name = name
        self.description = description
        self.dependencies = dependencies
        self.dev_dependencies = dev_dependencies
        self.license = license
        self.authors = authors

    def _stringify_dependencies(self, dependencies):
        return ", ".join(dependencies) if len(dependencies) > 0 else "-"

    def __str__(self):
        aut = f"Authors:"
        for x in self.authors:
            aut = aut +f"\n- "
            aut = aut + x
        deps = f"Dependencies:"
        for x in self.dependencies:
            deps = deps +f"\n- "
            deps = deps + x
        dev_deps = f"Dependencies:"
        for x in self.dependencies:
            dev_deps = dev_deps +f"\n- "
            dev_deps = dev_deps + x
        return (
            f"Name: {self.name}"
            f"\nDescription: {self.description or '-'}"
            f"\nLicense: {self.license}"
            f"\n"
            f"\n{aut}"
            f"\n"
            f"\n{deps}"
            f"\n"
            f"\n{dev_deps}"
            #f"\nDependencies: {self._stringify_dependencies(self.dependencies)}"
            #f"\nDevelopment dependencies: {self._stringify_dependencies(self.dev_dependencies)}"
            
       )
    
  
    

