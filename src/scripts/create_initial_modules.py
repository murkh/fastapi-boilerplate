import asyncio
import logging

from sqlalchemy import select

from ..app.core.db.database import AsyncSession, local_session
from ..app.models.module import Module

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

MODULES_TO_CREATE = [
    {"module_name": "Teams", "description": "Teams management module."},
    {"module_name": "E-Clinic", "description": "E-Clinic management module."},
    {"module_name": "Doctors", "description": "Doctor management module."},
    {"module_name": "Patients", "description": "Patient management module."},
    {"module_name": "Hospitals", "description": "Hospital management module."},
    {"module_name": "Corporates", "description": "Corporate management module."},
    {"module_name": "Health Camp", "description": "Health camp management module."},
    {
        "module_name": "Operation Dashboard",
        "description": "Operation dashboard module.",
    },
    {"module_name": "CMS", "description": "Content management system module."},
    {"module_name": "Resources", "description": "Resources management module."},
    {
        "module_name": "System Configuration",
        "description": "System configuration module.",
    },
    {"module_name": "Finance", "description": "Finance management module."},
    {"module_name": "Verification", "description": "Verification module."},
    {"module_name": "Reports", "description": "Reports module."},
    {
        "module_name": "Dashboard",
        "description": "Main dashboard for analytics and overview.",
    },
    {
        "module_name": "Import/Export",
        "description": "Handles import and export operations.",
    },
]


async def create_initial_modules(session: AsyncSession) -> None:
    try:
        for module_data in MODULES_TO_CREATE:
            query = select(Module).where(
                Module.module_name == module_data["module_name"]
            )
            result = await session.execute(query)
            module = result.scalar_one_or_none()
            if module is None:
                session.add(Module(**module_data, is_active=True))
                logger.info(f"Module '{module_data['module_name']}' created.")
            else:
                logger.info(f"Module '{module_data['module_name']}' already exists.")
        await session.commit()
        logger.info("Initial modules creation completed.")
    except Exception as e:
        logger.error(f"Error creating modules: {e}")


async def main():
    async with local_session() as session:
        await create_initial_modules(session)


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
