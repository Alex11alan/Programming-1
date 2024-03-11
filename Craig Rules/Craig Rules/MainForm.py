﻿import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self._label1 = System.Windows.Forms.Label()
		self.SuspendLayout()
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.Color.MistyRose
		self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.Location = System.Drawing.Point(12, 352)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(146, 89)
		self._button1.TabIndex = 0
		self._button1.Text = "Clear"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.Color.MistyRose
		self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button2.Location = System.Drawing.Point(164, 352)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(173, 89)
		self._button2.TabIndex = 1
		self._button2.Text = "Calculate"
		self._button2.UseVisualStyleBackColor = False
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.BackColor = System.Drawing.Color.MistyRose
		self._button3.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button3.Location = System.Drawing.Point(343, 352)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(140, 89)
		self._button3.TabIndex = 2
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = False
		self._button3.Click += self.Button3Click
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.Color.Coral
		self._label1.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
		self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 26.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label1.Location = System.Drawing.Point(31, 54)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(424, 237)
		self._label1.TabIndex = 3
		# 
		# MainForm
		# 
		self.ClientSize = System.Drawing.Size(495, 453)
		self.Controls.Add(self._label1)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Name = "MainForm"
		self.Text = "MainForm"
		self.ResumeLayout(False)


	def Button2Click(self, sender, e):
		self._label1.Text = "Craig Rules!"
	
	def Button1Click(self, sender, e):
		self._label1.Text = ""

	def Button3Click(self, sender, e):
		Application.Exit()