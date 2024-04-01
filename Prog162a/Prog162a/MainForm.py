﻿import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._label1 = System.Windows.Forms.Label()
		self._label2 = System.Windows.Forms.Label()
		self._label3 = System.Windows.Forms.Label()
		self._label4 = System.Windows.Forms.Label()
		self._textBox1 = System.Windows.Forms.TextBox()
		self._textBox2 = System.Windows.Forms.TextBox()
		self._label5 = System.Windows.Forms.Label()
		self._label6 = System.Windows.Forms.Label()
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self.SuspendLayout()
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.Color.MediumAquamarine
		self._label1.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
		self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label1.Location = System.Drawing.Point(13, 55)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(197, 45)
		self._label1.TabIndex = 0
		self._label1.Text = "Enter a number:"
		# 
		# label2
		# 
		self._label2.BackColor = System.Drawing.Color.SpringGreen
		self._label2.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
		self._label2.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label2.ForeColor = System.Drawing.Color.Black
		self._label2.Location = System.Drawing.Point(344, 61)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(197, 45)
		self._label2.TabIndex = 2
		self._label2.Text = " "
		# 
		# label3
		# 
		self._label3.BackColor = System.Drawing.Color.MediumAquamarine
		self._label3.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
		self._label3.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label3.Location = System.Drawing.Point(13, 156)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(197, 45)
		self._label3.TabIndex = 4
		self._label3.Text = "Enter a number:"
		# 
		# label4
		# 
		self._label4.BackColor = System.Drawing.Color.SpringGreen
		self._label4.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
		self._label4.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label4.ForeColor = System.Drawing.Color.Black
		self._label4.Location = System.Drawing.Point(344, 162)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(197, 45)
		self._label4.TabIndex = 3
		self._label4.Text = " "
		# 
		# textBox1
		# 
		self._textBox1.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
		self._textBox1.Location = System.Drawing.Point(216, 61)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(100, 20)
		self._textBox1.TabIndex = 5
		# 
		# textBox2
		# 
		self._textBox2.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
		self._textBox2.Location = System.Drawing.Point(216, 162)
		self._textBox2.Name = "textBox2"
		self._textBox2.Size = System.Drawing.Size(100, 20)
		self._textBox2.TabIndex = 6
		# 
		# label5
		# 
		self._label5.BackColor = System.Drawing.Color.MediumSpringGreen
		self._label5.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
		self._label5.Font = System.Drawing.Font("Microsoft Sans Serif", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label5.ForeColor = System.Drawing.Color.Black
		self._label5.Location = System.Drawing.Point(344, 134)
		self._label5.Name = "label5"
		self._label5.Size = System.Drawing.Size(197, 28)
		self._label5.TabIndex = 8
		self._label5.Text = " Output:"
		# 
		# label6
		# 
		self._label6.BackColor = System.Drawing.Color.MediumSpringGreen
		self._label6.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
		self._label6.Font = System.Drawing.Font("Microsoft Sans Serif", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label6.ForeColor = System.Drawing.Color.Black
		self._label6.Location = System.Drawing.Point(344, 33)
		self._label6.Name = "label6"
		self._label6.Size = System.Drawing.Size(197, 28)
		self._label6.TabIndex = 7
		self._label6.Text = " Output:"
		# 
		# button1
		# 
		self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.Location = System.Drawing.Point(13, 381)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(161, 139)
		self._button1.TabIndex = 9
		self._button1.Text = "Calculate"
		self._button1.UseVisualStyleBackColor = True
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button2.Location = System.Drawing.Point(206, 381)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(161, 139)
		self._button2.TabIndex = 10
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = True
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button3.Location = System.Drawing.Point(395, 381)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(161, 139)
		self._button3.TabIndex = 11
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = True
		self._button3.Click += self.Button3Click
		# 
		# MainForm
		# 
		self.ClientSize = System.Drawing.Size(568, 532)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._label5)
		self.Controls.Add(self._label6)
		self.Controls.Add(self._textBox2)
		self.Controls.Add(self._textBox1)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._label4)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._label1)
		self.Name = "MainForm"
		self.Text = "Prog162a"
		self.ResumeLayout(False)
		self.PerformLayout()


	def Button1Click(self, sender, e):
		pass

	def Button2Click(self, sender, e):
		self._textBox1.Text.Clear()
		self._textBox2.Text.Clear()
		self._label2.Text.Clear()
		self._label4.Text.Clear()

	def Button3Click(self, sender, e):
		Application.Exit()