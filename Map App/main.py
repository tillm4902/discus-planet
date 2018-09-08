# August 4, 2018
# discus-planet
# A website designed to be an interactible version of the Rhinus map

from google.appengine.ext import ndb

import jinja2
import os
import webapp2

jinja_env = jinja2.Environment(
    loader = jinja2.FileSystemLoader(os.path.dirname(__file__))
)

class MainHandler(webapp2.RequestHandler):
    def get(self):
        main_template = jinja_env.get_template('templates/main_page.html')
        html = main_template.render(
        )
        self.response.write(html)

class AndelorHandler(webapp2.RequestHandler):
    def get(self):
        andelor_template = jinja_env.get_template('templates/andelor.html')
        html = andelor_template.render(
        )
        self.response.write(html)

class ArienCommelHandler(webapp2.RequestHandler):
    def get(self):
        arien_commel_template = jinja_env.get_template('templates/arien_commel.html')
        html = arien_commel_template.render(
        )
        self.response.write(html)

class AshyeHandler(webapp2.RequestHandler):
    def get(self):
        ashye_template = jinja_env.get_template('templates/ashye.html')
        html = ashye_template.render(
        )
        self.response.write(html)

class AustrisHandler(webapp2.RequestHandler):
    def get(self):
        austris_template = jinja_env.get_template('templates/austris.html')
        html = austris_template.render(
        )
        self.response.write(html)

class BeelmarrHandler(webapp2.RequestHandler):
    def get(self):
        beelmarr_template = jinja_env.get_template('templates/beelmarr.html')
        html = beelmarr_template.render(
        )
        self.response.write(html)

class CastriaHandler(webapp2.RequestHandler):
    def get(self):
        castria_template = jinja_env.get_template('templates/castria.html')
        html = castria_template.render(
        )
        self.response.write(html)

class CorelemHandler(webapp2.RequestHandler):
    def get(self):
        corelem_template = jinja_env.get_template('templates/corelem.html')
        html = corelem_template.render(
        )
        self.response.write(html)

class CrandorHandler(webapp2.RequestHandler):
    def get(self):
        crandor_template = jinja_env.get_template('templates/crandor.html')
        html = crandor_template.render(
        )
        self.response.write(html)

class CrassiaHandler(webapp2.RequestHandler):
    def get(self):
        crassia_template = jinja_env.get_template('templates/crassia.html')
        html = crassia_template.render(
        )
        self.response.write(html)

class DahkatHandler(webapp2.RequestHandler):
    def get(self):
        dahkat_template = jinja_env.get_template('templates/dahkat.html')
        html = dahkat_template.render(
        )
        self.response.write(html)

class DorbenHandler(webapp2.RequestHandler):
    def get(self):
        dorben_template = jinja_env.get_template('templates/dorben.html')
        html = dorben_template.render(
        )
        self.response.write(html)

class DornfistHandler(webapp2.RequestHandler):
    def get(self):
        dornfist_template = jinja_env.get_template('templates/dornfist.html')
        html = dornfist_template.render(
        )
        self.response.write(html)

class DraksiliusHandler(webapp2.RequestHandler):
    def get(self):
        draksilius_template = jinja_env.get_template('templates/draksilius.html')
        html = draksilius_template.render(
        )
        self.response.write(html)

class DuelforHandler(webapp2.RequestHandler):
    def get(self):
        duelfor_template = jinja_env.get_template('templates/duelfor.html')
        html = duelfor_template.render(
        )
        self.response.write(html)

class EmpirusHandler(webapp2.RequestHandler):
    def get(self):
        empirus_template = jinja_env.get_template('templates/empirus.html')
        html = empirus_template.render(
        )
        self.response.write(html)

class EstrenHandler(webapp2.RequestHandler):
    def get(self):
        estren_template = jinja_env.get_template('templates/estren.html')
        html = estren_template.render(
        )
        self.response.write(html)

class FareldonHandler(webapp2.RequestHandler):
    def get(self):
        fareldon_template = jinja_env.get_template('templates/fareldon.html')
        html = fareldon_template.render(
        )
        self.response.write(html)

class FeyelderHandler(webapp2.RequestHandler):
    def get(self):
        feyelder_template = jinja_env.get_template('templates/feyelder.html')
        html = feyelder_template.render(
        )
        self.response.write(html)

class FheridHandler(webapp2.RequestHandler):
    def get(self):
        fherid_template = jinja_env.get_template('templates/fherid.html')
        html = fherid_template.render(
        )
        self.response.write(html)

class FrailorHandler(webapp2.RequestHandler):
    def get(self):
        frailor_template = jinja_env.get_template('templates/frailor.html')
        html = frailor_template.render(
        )
        self.response.write(html)

class FreetownHandler(webapp2.RequestHandler):
    def get(self):
        freetown_template = jinja_env.get_template('templates/freetown.html')
        html = freetown_template.render(
        )
        self.response.write(html)

class FriziaHandler(webapp2.RequestHandler):
    def get(self):
        frizia_template = jinja_env.get_template('templates/frizia.html')
        html = frizia_template.render(
        )
        self.response.write(html)

class GrodEzudHandler(webapp2.RequestHandler):
    def get(self):
        grod_ezud_template = jinja_env.get_template('templates/grod_ezud.html')
        html = grod_ezud_template.render(
        )
        self.response.write(html)

class GrodLadhidHandler(webapp2.RequestHandler):
    def get(self):
        grod_ladidh_template = jinja_env.get_template('templates/grod_ladidh.html')
        html = grod_ladidh_template.render(
        )
        self.response.write(html)

class GrodNuranHandler(webapp2.RequestHandler):
    def get(self):
        grod_nuran_template = jinja_env.get_template('templates/grod_nuran.html')
        html = grod_nuran_template.render(
        )
        self.response.write(html)

class HammerforgeHandler(webapp2.RequestHandler):
    def get(self):
        hammerforge_template = jinja_env.get_template('templates/hammerforge.html')
        html = hammerforge_template.render(
        )
        self.response.write(html)

class HeironHandler(webapp2.RequestHandler):
    def get(self):
        heiron_template = jinja_env.get_template('templates/heiron.html')
        html = heiron_template.render(
        )
        self.response.write(html)

class HekellHandler(webapp2.RequestHandler):
    def get(self):
        hekell_template = jinja_env.get_template('templates/hekell.html')
        html = hekell_template.render(
        )
        self.response.write(html)

class HorspusHandler(webapp2.RequestHandler):
    def get(self):
        horspus_template = jinja_env.get_template('templates/horspus.html')
        html = horspus_template.render(
        )
        self.response.write(html)

class HuikHandler(webapp2.RequestHandler):
    def get(self):
        huik_template = jinja_env.get_template('templates/huik.html')
        html = huik_template.render(
        )
        self.response.write(html)

class IronhallHandler(webapp2.RequestHandler):
    def get(self):
        ironhall_template = jinja_env.get_template('templates/ironhall.html')
        html = ironhall_template.render(
        )
        self.response.write(html)

class IstrielHandler(webapp2.RequestHandler):
    def get(self):
        istriel_template = jinja_env.get_template('templates/istriel.html')
        html = istriel_template.render(
        )
        self.response.write(html)

class KaleforgeHandler(webapp2.RequestHandler):
    def get(self):
        kaleforge_template = jinja_env.get_template('templates/kaleforge.html')
        html = kaleforge_template.render(
        )
        self.response.write(html)

class KanaitaHandler(webapp2.RequestHandler):
    def get(self):
        kanaita_template = jinja_env.get_template('templates/kanaita.html')
        html = kanaita_template.render(
        )
        self.response.write(html)

class KeratorHandler(webapp2.RequestHandler):
    def get(self):
        kerator_template = jinja_env.get_template('templates/kerator.html')
        html = kerator_template.render(
        )
        self.response.write(html)

class KoriusHandler(webapp2.RequestHandler):
    def get(self):
        korius_template = jinja_env.get_template('templates/korius.html')
        html = korius_template.render(
        )
        self.response.write(html)

class KrayelHandler(webapp2.RequestHandler):
    def get(self):
        krayel_template = jinja_env.get_template('templates/krayel.html')
        html = krayel_template.render(
        )
        self.response.write(html)

class MarkallHandler(webapp2.RequestHandler):
    def get(self):
        markall_template = jinja_env.get_template('templates/markall.html')
        html = markall_template.render(
        )
        self.response.write(html)

class MarocHandler(webapp2.RequestHandler):
    def get(self):
        maroc_template = jinja_env.get_template('templates/maroc.html')
        html = maroc_template.render(
        )
        self.response.write(html)

class NarforellHandler(webapp2.RequestHandler):
    def get(self):
        narforell_template = jinja_env.get_template('templates/narforell.html')
        html = narforell_template.render(
        )
        self.response.write(html)

class OstoriaHandler(webapp2.RequestHandler):
    def get(self):
        ostoria_template = jinja_env.get_template('templates/ostoria.html')
        html = ostoria_template.render(
        )
        self.response.write(html)

class PasalHandler(webapp2.RequestHandler):
    def get(self):
        pasal_template = jinja_env.get_template('templates/pasal.html')
        html = pasal_template.render(
        )
        self.response.write(html)

class PassilHandler(webapp2.RequestHandler):
    def get(self):
        passil_template = jinja_env.get_template('templates/passil.html')
        html = passil_template.render(
        )
        self.response.write(html)

class PleicorHandler(webapp2.RequestHandler):
    def get(self):
        pleicor_template = jinja_env.get_template('templates/pleicor.html')
        html = pleicor_template.render(
        )
        self.response.write(html)

class PrestigiaHandler(webapp2.RequestHandler):
    def get(self):
        prestigia_template = jinja_env.get_template('templates/prestigia.html')
        html = prestigia_template.render(
        )
        self.response.write(html)

class RayforgeHandler(webapp2.RequestHandler):
    def get(self):
        rayforge_template = jinja_env.get_template('templates/rayforge.html')
        html = rayforge_template.render(
        )
        self.response.write(html)

class RiefellHandler(webapp2.RequestHandler):
    def get(self):
        riefell_template = jinja_env.get_template('templates/riefell.html')
        html = riefell_template.render(
        )
        self.response.write(html)

class SfarlukHandler(webapp2.RequestHandler):
    def get(self):
        sfarluk_template = jinja_env.get_template('templates/sfarluk.html')
        html = sfarluk_template.render(
        )
        self.response.write(html)

class SkellforHandler(webapp2.RequestHandler):
    def get(self):
        skellfor_template = jinja_env.get_template('templates/skellfor.html')
        html = skellfor_template.render(
        )
        self.response.write(html)

class SmithellHandler(webapp2.RequestHandler):
    def get(self):
        smithell_template = jinja_env.get_template('templates/smithell.html')
        html = smithell_template.render(
        )
        self.response.write(html)

class SparseColoniesHandler(webapp2.RequestHandler):
    def get(self):
        sparse_colonies_template = jinja_env.get_template('templates/sparse_colonies.html')
        html = sparse_colonies_template.render(
        )
        self.response.write(html)

class TaelnaesHandler(webapp2.RequestHandler):
    def get(self):
        taelnaes_template = jinja_env.get_template('templates/taelnaes.html')
        html = taelnaes_template.render(
        )
        self.response.write(html)

class TarrielHandler(webapp2.RequestHandler):
    def get(self):
        tarriel_template = jinja_env.get_template('templates/tarriel.html')
        html = tarriel_template.render(
        )
        self.response.write(html)

class TelienHandler(webapp2.RequestHandler):
    def get(self):
        telien_template = jinja_env.get_template('templates/telien.html')
        html = telien_template.render(
        )
        self.response.write(html)

class ThiemalHandler(webapp2.RequestHandler):
    def get(self):
        thiemal_template = jinja_env.get_template('templates/thiemal.html')
        html = thiemal_template.render(
        )
        self.response.write(html)

class TilhamusHandler(webapp2.RequestHandler):
    def get(self):
        tilhamus_template = jinja_env.get_template('templates/tilhamus.html')
        html = tilhamus_template.render(
        )
        self.response.write(html)

class TinkerforgeHandler(webapp2.RequestHandler):
    def get(self):
        tinkerforge_template = jinja_env.get_template('templates/tinkerforge.html')
        html = tinkerforge_template.render(
        )
        self.response.write(html)

class TrileaHandler(webapp2.RequestHandler):
    def get(self):
        trilea_template = jinja_env.get_template('templates/trilea.html')
        html = trilea_template.render(
        )
        self.response.write(html)

class TsorienHandler(webapp2.RequestHandler):
    def get(self):
        tsorien_template = jinja_env.get_template('templates/tsorien.html')
        html = tsorien_template.render(
        )
        self.response.write(html)

class VaridelHandler(webapp2.RequestHandler):
    def get(self):
        varidel_template = jinja_env.get_template('templates/varidel.html')
        html = varidel_template.render(
        )
        self.response.write(html)

class VenturaHandler(webapp2.RequestHandler):
    def get(self):
        ventura_template = jinja_env.get_template('templates/ventura.html')
        html = ventura_template.render(
        )
        self.response.write(html)

class YureiamHandler(webapp2.RequestHandler):
    def get(self):
        yureiam_template = jinja_env.get_template('templates/yureiam.html')
        html = yureiam_template.render(
        )
        self.response.write(html)

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/andelor', AndelorHandler),
    ('/arien_commel', ArienCommelHandler),
    ('/ashye', AshyeHandler),
    ('/austris', AustrisHandler),
    ('/beelmarr', BeelmarrHandler),
    ('/castria', CastriaHandler),
    ('/crassia', CrassiaHandler),
    ('/dahkat', DahkatHandler),
    ('/dorben', DorbenHandler),
    ('/draksilius', DraksiliusHandler),
    ('/duelfor', DuelforHandler),
    ('/empirus', EmpirusHandler),
    ('/estren', EstrenHandler),
    ('/fareldon', FareldonHandler),
    ('/feyelder', FeyelderHandler),
    ('/fherid', FheridHandler),
    ('/frailor', FrailorHandler),
    ('/freetown', FreetownHandler),
    ('/frizia', FriziaHandler),
    ('/grod_ezud', GrodEzudHandler),
    ('/grod_ladhid', GrodLadhidHandler),
    ('/grod_nuran', GrodNuranHandler),
    ('/hammerforge', HammerforgeHandler),
    ('/heiron', HeironHandler),
    ('/hekell', HekellHandler),
    ('/horspus', HorspusHandler),
    ('/huik', HuikHandler),
    ('/ironhall', IronhallHandler),
    ('/istriel', IstrielHandler),
    ('/kaleforge', KaleforgeHandler),
    ('/kanaita', KanaitaHandler),
    ('/kerator', KeratorHandler),
    ('/korius', KoriusHandler),
    ('/krayel', KrayelHandler),
    ('/markall', MarkallHandler),
    ('/maroc', MarocHandler),
    ('/narforell', NarforellHandler),
    ('/ostoria', OstoriaHandler),
    ('/pasal', PasalHandler),
    ('/passil', PassilHandler),
    ('/pleicor', PleicorHandler),
    ('/prestigia', PrestigiaHandler),
    ('/rayforge', RayforgeHandler),
    ('/riefell', RiefellHandler),
    ('/sfarluk', SfarlukHandler),
    ('/skellfor', SkellforHandler),
    ('/smithell', SmithellHandler),
    ('/sparse_colonies', SparseColoniesHandler),
    ('/taelnaes', TaelnaesHandler),
    ('/tarriel', TarrielHandler),
    ('/telien', TelienHandler),
    ('/thiemal', ThiemalHandler),
    ('/tilhamus', TilhamusHandler),
    ('/tinkerforge', TinkerforgeHandler),
    ('/trilea', TrileaHandler),
    ('/tsorien', TsorienHandler),
    ('/varidel', VaridelHandler),
    ('/ventura', VenturaHandler),
    ('/yureiam', YureiamHandler)
], debug=True)
