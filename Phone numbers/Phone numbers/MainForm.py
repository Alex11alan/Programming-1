import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._label1 = System.Windows.Forms.Label()
		self._label2 = System.Windows.Forms.Label()
		self._label3 = System.Windows.Forms.Label()
		self._label4 = System.Windows.Forms.Label()
		self._label5 = System.Windows.Forms.Label()
		self._button3 = System.Windows.Forms.Button()
		self.SuspendLayout()
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.Color.Turquoise
		self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.Location = System.Drawing.Point(12, 386)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(132, 56)
		self._button1.TabIndex = 0
		self._button1.Text = "Clear"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.Color.Turquoise
		self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button2.Location = System.Drawing.Point(150, 386)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(240, 56)
		self._button2.TabIndex = 1
		self._button2.Text = "Calculate"
		self._button2.UseVisualStyleBackColor = False
		self._button2.Click += self.Button2Click
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.Color.LightSkyBlue
		self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label1.Location = System.Drawing.Point(32, 51)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(237, 34)
		self._label1.TabIndex = 3
		# 
		# label2
		# 
		self._label2.BackColor = System.Drawing.Color.LightSkyBlue
		self._label2.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label2.Location = System.Drawing.Point(32, 107)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(237, 34)
		self._label2.TabIndex = 4
		# 
		# label3
		# 
		self._label3.BackColor = System.Drawing.Color.LightSkyBlue
		self._label3.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label3.Location = System.Drawing.Point(32, 168)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(237, 34)
		self._label3.TabIndex = 5
		# 
		# label4
		# 
		self._label4.BackColor = System.Drawing.Color.LightSkyBlue
		self._label4.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label4.Location = System.Drawing.Point(32, 224)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(237, 34)
		self._label4.TabIndex = 6
		# 
		# label5
		# 
		self._label5.BackColor = System.Drawing.Color.LightSkyBlue
		self._label5.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label5.Location = System.Drawing.Point(32, 282)
		self._label5.Name = "label5"
		self._label5.Size = System.Drawing.Size(237, 34)
		self._label5.TabIndex = 7
		# 
		# button3
		# 
		self._button3.BackColor = System.Drawing.Color.Turquoise
		self._button3.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button3.Location = System.Drawing.Point(396, 386)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(132, 56)
		self._button3.TabIndex = 8
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = False
		self._button3.Click += self.Button3Click
		# 
		# MainForm
		# 
		self.ClientSize = System.Drawing.Size(540, 454)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._label5)
		self.Controls.Add(self._label4)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._label1)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Name = "MainForm"
		self.Text = "MainForm"
		self.ResumeLayout(False)


	def Button2Click(self, sender, e):
		self._label1.Text = "(608) 743-5200"
		self._label2.Text = "1 (800) 925-6278"
		self._label3.Text = "1 (800) 948-8488"
		self._label4.Text = "1 (800) 822-6235"
		self._label5.Text = "(608) 754-4096"
	
	def Button1Click(self, sender, e):
		self._label1.Text = ""
		self._label2.Text = ""
		self._label3.Text = ""
		self._label4.Text = ""
		self._label5.Text = ""
		
	def Button3Click(self, sender, e):
		Application.Exit()


	