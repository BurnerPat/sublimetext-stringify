import sublime, sublime_plugin
import re

class StringifyJava(sublime_plugin.TextCommand):
	def run(self, edit):
		for region in self.view.sel():
			if not region.empty():
				text = re.sub(r'([\\"])', r'\\\1', self.view.substr(region))
				self.view.replace(edit, region, text)