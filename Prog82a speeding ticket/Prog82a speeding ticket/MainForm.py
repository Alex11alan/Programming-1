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
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self._textBox1 = System.Windows.Forms.TextBox()
		self._textBox2 = System.Windows.Forms.TextBox()
		self._label5 = System.Windows.Forms.Label()
		self._label6 = System.Windows.Forms.Label()
		self.SuspendLayout()
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.Color.Bisque
		self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label1.Location = System.Drawing.Point(25, 24)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(173, 36)
		self._label1.TabIndex = 0
		self._label1.Text = "Speed limit:"
		# 
		# label2
		# 
		self._label2.BackColor = System.Drawing.Color.Bisque
		self._label2.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label2.Location = System.Drawing.Point(25, 76)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(173, 36)
		self._label2.TabIndex = 1
		self._label2.Text = " Vehicle speed:"
		# 
		# button1
		# 
		self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.Location = System.Drawing.Point(189, 266)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(149, 112)
		self._button1.TabIndex = 6
		self._button1.Text = "Clear"
		self._button1.UseVisualStyleBackColor = True
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button2.Location = System.Drawing.Point(34, 266)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(149, 112)
		self._button2.TabIndex = 7
		self._button2.Text = "Calculate"
		self._button2.UseVisualStyleBackColor = True
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button3.Location = System.Drawing.Point(344, 266)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(149, 112)
		self._button3.TabIndex = 8
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = True
		self._button3.Click += self.Button3Click
		# 
		# textBox1
		# 
		self._textBox1.Location = System.Drawing.Point(294, 40)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(173, 20)
		self._textBox1.TabIndex = 9
		# 
		# textBox2
		# 
		self._textBox2.Location = System.Drawing.Point(294, 92)
		self._textBox2.Name = "textBox2"
		self._textBox2.Size = System.Drawing.Size(173, 20)
		self._textBox2.TabIndex = 10
		# 
		# label5
		# 
		self._label5.BackColor = System.Drawing.Color.Bisque
		self._label5.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label5.Location = System.Drawing.Point(294, 129)
		self._label5.Name = "label5"
		self._label5.Size = System.Drawing.Size(173, 36)
		self._label5.TabIndex = 12
		self._label5.Text = " "
		# 
		# label6
		# 
		self._label6.BackColor = System.Drawing.Color.Bisque
		self._label6.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label6.Location = System.Drawing.Point(25, 129)
		self._label6.Name = "label6"
		self._label6.Size = System.Drawing.Size(173, 36)
		self._label6.TabIndex = 11
		self._label6.Text = " Total Fine:"
		# 
		# MainForm
		# 
		self.ClientSize = System.Drawing.Size(529, 407)
		self.Controls.Add(self._label5)
		self.Controls.Add(self._label6)
		self.Controls.Add(self._textBox2)
		self.Controls.Add(self._textBox1)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._label1)
		self.Name = "MainForm"
		self.Text = "Prog82a speeding ticket"
		self.ResumeLayout(False)
		self.PerformLayout()


	def Button2Click(self, sender, e):
		spdlim = int(self._textBox1.Text)
		vhspd = int(self._textBox2.Text)
		fine = 0.00
		if vhspd == 10 > spdlim:
			fine = 20.00
		elif vhspd == spdlim:
			fine = 0.00
		mo = vhspd - spdlim
		motp = mo * 5
		totalfine = motp + fine
		
		self._label5.Text = str(totalfine)
	
	def Button1Click(self, sender, e):
		self._textBox1.Text = ""
		self._textBox2.Text = ""
		self._label5.Text = ""

	def Button3Click(self, sender, e):
		Application.Exit()
		