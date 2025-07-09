from .api import router
from .core.config import settings
from .core.setup import create_application
from dotenv import load_dotenv

load_dotenv()

app = create_application(router=router, settings=settings)
