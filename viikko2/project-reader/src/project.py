class Project:
    def __init__(self, name, description, license, authors, dependencies, dev_dependencies):
        self.name = name
        self.description = description
        self.license = license
        self.authors = authors
        self.dependencies = dependencies
        self.dev_dependencies = dev_dependencies

    def _seperate_dependencies(self, dependencies):
        list_dependencies = list(dependencies.keys())
        result_dependencies = ""
        for dependency in list_dependencies:
            result_dependencies += f"\n - {dependency}"
        return result_dependencies

    
    def _seperate_list_items(self, authors):
        result_authors = ""
        for author in authors:
            result_authors += f"\n - {author}"
        return result_authors


    def __str__(self):
        return (
            f"Name: {self.name}"
            f"\nDescription: {self.description or '-'}"
            f"\nLicense: {self.license}"
            f"\n"
            f"\nAuthors: {self._seperate_list_items(self.authors)}"
            f"\n"
            f"\nDependencies: {self._seperate_dependencies(self.dependencies)}"
            f"\n"
            f"\nDevelopment dependencies: {self._seperate_dependencies(self.dev_dependencies)}"
        )
