from selenium.webdriver import ActionChains

from Browser import Browser

draggable="draggable"
droppable="droppable"
class draganddrop (Browser):
    def drag (self):
        source1 = self.driver.find_element_by_id(draggable)
        action = ActionChains(self.driver)
        action.drag_and_drop_by_offset(source1, 134, 20).perform()
        target1 = self.driver.find_element_by_id(droppable)
