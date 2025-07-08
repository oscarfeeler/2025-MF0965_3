from persistence import CountryRepository


class CountryService:
    def __init__(self):
        self.repo = CountryRepository()

    def list_country(self):
        # Aquí podrías filtrar, paginar, formatear datos, etc.
        return self.repo.fetch_all()

    def remove_country(self, Code):
        # Validaciones previas (por ej. comprobar existencia)
        self.repo.delete(Code)

    # añadir métodos create_customer, update_customer, etc.
    def add_country(self, datos_pais):
        self.repo.add(datos_pais)