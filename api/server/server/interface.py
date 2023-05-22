from abc import ABC, abstractmethod

class RenderTemplateInterface(ABC):
    @abstractmethod
    def render_template(self, template_name: str, **kwargs) -> str:
        pass
