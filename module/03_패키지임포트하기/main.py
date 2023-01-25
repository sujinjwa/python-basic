# 첫번째 방법: import 패키지.모듈
import unit.character
unit.character.test() # this is a character module

# 두번째 방법: from 패키지 import 모듈 (가장 많이 사용)
from unit import item
item.test() # this is an item module

# 3~4번째 방법은 __init__.py에서의 from . import character, item, monster 코드 필요

# 세번째 방법: from 패키지 import *
from unit import *
monster.test() # this is a monster module

# 네번째 방법: import 패키지
import unit
unit.character.test() # this is a character module
unit.item.test() # this is an itemmodule
unit.monster.test() # this is a monster module