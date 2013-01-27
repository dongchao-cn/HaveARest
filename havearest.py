#! /usr/bin/env python
# -*- coding: utf8 -*- 
import time
import wx
import thread

workingTime = 5 # workingTime second
restTime = 3 # restTime second

class MyFrame(wx.Frame): 
	def __init__(self,work,rest):
		wx.Frame.__init__(self, None, -1, "My Frame", size=(300, 300))
		panel = wx.Panel(self, -1)
		wx.StaticText(panel, -1, "HaveARest!", pos=(10, 12))
		thread.start_new(self.Loop,(work,rest))

	def Loop(self,work,rest):
		workCount = 0
		while 1:
			if workCount >= work:
				# have a rest
				workCount = 0
				restCount = rest
				while restCount > 0:
					# block the screen
					self.blockScreen()
					restCount -= 1
					time.sleep(1)
					print "resttime"
				# release the screen
				self.releaseScreen()
			else:
				workCount += 1
				time.sleep(1)
				print "workingtime"

	def OnExit(self):
		print "Exit"
		return True

	def blockScreen(self):
		print "blockScreen"
		self.Show(True)

	def releaseScreen(self):
		print "releaseScreen"
		self.Show(False)

if __name__ == '__main__':
	app = wx.PySimpleApp()
	frame = MyFrame(workingTime,restTime)
	frame.Show(True)
	frame.Show(False)
	app.MainLoop()

