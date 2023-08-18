from .  import openAI_east_us_03
from .  import openAI_east_us_02
from .  import openAI_east_us_01

from .  import openAI_sc_us_01
from .  import openAI_sc_us_02
from .  import openAI_sc_us_03
from .  import eventCreationFromTitle

gpt4Openaieastus01 = openAI_east_us_01.gpt4Openaieastus01
gpt4Openaieastus02 = openAI_east_us_02.gpt4Openaieastus02
gpt4Openaieastus03 = openAI_east_us_03.gpt4Openaieastus03
gpt4Openaiscus01 = openAI_sc_us_01.gpt4Openaiscus01
gpt4Openaiscus02 = openAI_sc_us_02.gpt4Openaiscus02
gpt4Openaiscus03 = openAI_sc_us_03.gpt4Openaiscus03
eventCreateByTitle = eventCreationFromTitle.eventCreateByTitle

__all__ = ['gpt4Openaieastus01','gpt4Openaieastus02','gpt4Openaieastus03','gpt4Openaiscus01','gpt4Openaiscus02','gpt4Openaiscus03','eventCreateByTitle']