import pygetwindow as gw
import time


windows = gw.getAllWindows()
class Window:
    def __init__(self):
        pass

    def get_window_by_title(self, title):
        windows = gw.getWindowsWithTitle(title)
        if windows:
            return windows[0]
        else:
            return None

    def activate_window(self, window):
        try:
            if window:
                window.activate()
                
        except Exception as e:
            print(f"Error in activating window: {e}")
            
            
    def close_window(app_name):
        try:
            windows_list = gw.getWindowsWithTitle(app_name)

            if windows_list:
                windows_list[0].close()
                
        except Exception as e:
            print(f"Error in closing window: {e}")
    
    def minimize_window(self):
        try:
            visible_windows = [
            w for w in gw.getAllWindows()
            if w.title.strip() and not w.isMinimized
            ]

            for w in visible_windows:
                w.minimize()
                
        except Exception as e:
            print(f"Error in minimizing window: {e}")
            
    import pygetwindow as gw

    def maximize_window(self, app_name):
        try:
            # Convert voice command to lowercase
            app_name = app_name.lower().strip()

            # Common aliases
            aliases = {
                "microsoft edge": "edge",
                "edge": "edge",
                "google chrome": "chrome",
                "chrome": "chrome",
                "vs code": "visual studio code",
                "visual studio code": "visual studio code",
                "code": "visual studio code",
                "notepad": "notepad",
                "spotify": "spotify",
            }

            search = aliases.get(app_name, app_name)

            # Get all windows with titles
            windows = [w for w in gw.getAllWindows() if w.title.strip()]

            target = None

            for w in windows:
                title = w.title.lower()

                if search in title:
                    target = w
                    break

            if target is None:
                print(f"❌ No window found containing '{search}'")

                print("\nAvailable windows:")
                for w in windows:
                    print("-", w.title)

                return False

            # Restore if minimized
            if target.isMinimized:
                target.restore()
                time.sleep(0.5)

            # Maximize if not already maximized
            if not target.isMaximized:
                target.maximize()

            target.activate()

            print(f"✅ Maximized: {target.title}")
            return True

        except Exception as e:
            print("Error while maximizing window:", e)
            return False
                
                
        
            

