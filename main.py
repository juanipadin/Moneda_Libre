from kivy.app import App
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.lang import Builder
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from dolarblue import dolarblue
#from dolarDAI import dolarDAI
from dolarsolidario import dolarSoli

kv = Builder.load_file('main.kv')
class MainWid(ScreenManager):
    def press_oficial(self):
        oficial = self.ids.name_input.text
        oficial_float = float(oficial)
        self.ids.name_label.text = str("Ud. Podrá Adquirir U$D "+str(f"{round((oficial_float / dolarSoli), 2):,}"))

    def press_blue(self):
        blue = self.ids.name_input.text
        blue_float = float(blue)
        self.ids.name_label.text = str("Ud. Podrá Adquirir U$D "+str(f"{round((blue_float / dolarblue), 2):,}"))

    #def press_dai(self):
    #    dai = self.ids.name_input.text
    #    dai_float = float(dai)
    #    self.ids.name_label.text = str("Ud. Podrá Adquirir U$D "+str(f"{round((dai_float / dolarDAI), 2):,}"))

    def valor_dolarsolidario(self):
        return "La Cotizacion del Dolar Solidario es de $" + str(dolarSoli)

    def valor_dolarblue(self):
        return "La Cotizacion del Dolar Blue es de $" + str(dolarblue)

    #def valor_dolardai(self):
    #    return "La Cotizacion del Dolar DAI es de $" + str(dolarDAI)
class MainScreen(Screen):
    pass

class MonedalibrelApp(App):
    title="Moneda Libre"
    def build(self):
        return MainWid()

if __name__ == "__main__":
    MonedalibrelApp().run()