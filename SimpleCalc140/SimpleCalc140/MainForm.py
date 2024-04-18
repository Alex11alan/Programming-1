import math
import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._label1 = System.Windows.Forms.Label()
		self._label2 = System.Windows.Forms.Label()
		self._button7 = System.Windows.Forms.Button()
		self._button8 = System.Windows.Forms.Button()
		self._button9 = System.Windows.Forms.Button()
		self._label3 = System.Windows.Forms.Label()
		self._textBox1 = System.Windows.Forms.TextBox()
		self._textBox2 = System.Windows.Forms.TextBox()
		self._label4 = System.Windows.Forms.Label()
		self._label5 = System.Windows.Forms.Label()
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self._button6 = System.Windows.Forms.Button()
		self._button5 = System.Windows.Forms.Button()
		self._button4 = System.Windows.Forms.Button()
		self.SuspendLayout()
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.Color.AliceBlue
		self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label1.Location = System.Drawing.Point(12, 9)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(127, 59)
		self._label1.TabIndex = 0
		self._label1.Text = "Number 1:"
		# 
		# label2
		# 
		self._label2.BackColor = System.Drawing.Color.AliceBlue
		self._label2.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label2.Location = System.Drawing.Point(12, 167)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(127, 59)
		self._label2.TabIndex = 1
		self._label2.Text = "Number 2:"
		# 
		# button7
		# 
		self._button7.Font = System.Drawing.Font("Microsoft Sans Serif", 26.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button7.Location = System.Drawing.Point(373, 195)
		self._button7.Name = "button7"
		self._button7.Size = System.Drawing.Size(162, 65)
		self._button7.TabIndex = 8
		self._button7.Text = "MOD"
		self._button7.UseVisualStyleBackColor = True
		self._button7.Click += self.Button7Click
		# 
		# button8
		# 
		self._button8.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button8.Location = System.Drawing.Point(373, 332)
		self._button8.Name = "button8"
		self._button8.Size = System.Drawing.Size(162, 65)
		self._button8.TabIndex = 7
		self._button8.Text = "Clear"
		self._button8.UseVisualStyleBackColor = True
		self._button8.Click += self.Button8Click
		# 
		# button9
		# 
		self._button9.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button9.Location = System.Drawing.Point(373, 403)
		self._button9.Name = "button9"
		self._button9.Size = System.Drawing.Size(162, 65)
		self._button9.TabIndex = 6
		self._button9.Text = "Exit"
		self._button9.UseVisualStyleBackColor = True
		self._button9.Click += self.Button9Click
		# 
		# label3
		# 
		self._label3.BackColor = System.Drawing.Color.AliceBlue
		self._label3.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label3.Location = System.Drawing.Point(12, 321)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(127, 59)
		self._label3.TabIndex = 9
		self._label3.Text = "Sum:"
		# 
		# textBox1
		# 
		self._textBox1.Location = System.Drawing.Point(146, 31)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(178, 20)
		self._textBox1.TabIndex = 10
		# 
		# textBox2
		# 
		self._textBox2.Location = System.Drawing.Point(146, 195)
		self._textBox2.Name = "textBox2"
		self._textBox2.Size = System.Drawing.Size(178, 20)
		self._textBox2.TabIndex = 11
		# 
		# label4
		# 
		self._label4.Location = System.Drawing.Point(181, 83)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(100, 84)
		self._label4.TabIndex = 12
		# 
		# label5
		# 
		self._label5.BackColor = System.Drawing.Color.Beige
		self._label5.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label5.Location = System.Drawing.Point(146, 321)
		self._label5.Name = "label5"
		self._label5.Size = System.Drawing.Size(205, 59)
		self._label5.TabIndex = 13
		# 
		# button1
		# 
		self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.Location = System.Drawing.Point(340, 31)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(75, 65)
		self._button1.TabIndex = 0
		self._button1.Text = "+"
		self._button1.UseVisualStyleBackColor = True
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button2.Location = System.Drawing.Point(421, 31)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(75, 65)
		self._button2.TabIndex = 1
		self._button2.Text = "-"
		self._button2.UseVisualStyleBackColor = True
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button3.Location = System.Drawing.Point(502, 31)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(75, 65)
		self._button3.TabIndex = 2
		self._button3.Text = "="
		self._button3.UseVisualStyleBackColor = True
		self._button3.Click += self.Button3Click
		# 
		# button6
		# 
		self._button6.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button6.Location = System.Drawing.Point(502, 102)
		self._button6.Name = "button6"
		self._button6.Size = System.Drawing.Size(75, 65)
		self._button6.TabIndex = 3
		self._button6.Text = "//"
		self._button6.UseVisualStyleBackColor = True
		self._button6.Click += self.Button6Click
		# 
		# button5
		# 
		self._button5.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button5.Location = System.Drawing.Point(421, 102)
		self._button5.Name = "button5"
		self._button5.Size = System.Drawing.Size(75, 65)
		self._button5.TabIndex = 4
		self._button5.Text = "/"
		self._button5.UseVisualStyleBackColor = True
		self._button5.Click += self.Button5Click
		# 
		# button4
		# 
		self._button4.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button4.Location = System.Drawing.Point(340, 102)
		self._button4.Name = "button4"
		self._button4.Size = System.Drawing.Size(75, 65)
		self._button4.TabIndex = 5
		self._button4.Text = "^"
		self._button4.UseVisualStyleBackColor = True
		self._button4.Click += self.Button4Click
		# 
		# MainForm
		# 
		self.ClientSize = System.Drawing.Size(589, 506)
		self.Controls.Add(self._button4)
		self.Controls.Add(self._label5)
		self.Controls.Add(self._button5)
		self.Controls.Add(self._label4)
		self.Controls.Add(self._button6)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._textBox2)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._textBox1)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._button7)
		self.Controls.Add(self._button8)
		self.Controls.Add(self._button9)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._label1)
		self.Name = "MainForm"
		self.Text = "SimpleCalc140"
		self.ResumeLayout(False)
		self.PerformLayout()


	def Button1Click(self, sender, e):
		v1 = int(self._textBox1.Text)
		v2 = int(self._textBox2.Text)
		c = str(v1 + v2)
		self._label5.Text = c

	def Button2Click(self, sender, e):
		v1 = int(self._textBox1.Text)
		v2 = int(self._textBox2.Text)
		c = str(v1 - v2)
		self._label5.Text = c

	def Button3Click(self, sender, e):
		v1 = int(self._textBox1.Text)
		v2 = int(self._textBox2.Text)

	def Button4Click(self, sender, e):
		v1 = int(self._textBox1.Text)
		v2 = int(self._textBox2.Text)
		c = str(v1 * v2)
		self._label5.Text = c

	def Button5Click(self, sender, e):
		v1 = int(self._textBox1.Text)
		v2 = int(self._textBox2.Text)
		c = str(v1 / v2)
		self._label5.Text = c

	def Button6Click(self, sender, e):
		v1 = int(self._textBox1.Text)
		v2 = int(self._textBox2.Text)
		c = str(v1 // v2)
		self._label5.Text = c
		
	def Button7Click(self, sender, e):
		v1 = int(self._textBox1.Text)
		v2 = int(self._textBox2.Text)
		c = str(abs(v1 - v2))
		self._label5.Text = c

	def Button8Click(self, sender, e):
		self._textBox1.Text = ""
		self._textBox2.Text = ""
		self._label5.Text = ""
	
	def Button9Click(self, sender, e):
		Application.Exit()