import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._label1 = System.Windows.Forms.Label()
		self._button1 = System.Windows.Forms.Button()
		self._label2 = System.Windows.Forms.Label()
		self._label3 = System.Windows.Forms.Label()
		self._label4 = System.Windows.Forms.Label()
		self._textBox1 = System.Windows.Forms.TextBox()
		self._textBox2 = System.Windows.Forms.TextBox()
		self.SuspendLayout()
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.Color.Chocolate
		self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label1.Location = System.Drawing.Point(27, 36)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(153, 49)
		self._label1.TabIndex = 0
		self._label1.Text = "Annual Salary:"
		# 
		# button1
		# 
		self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.Location = System.Drawing.Point(151, 301)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(135, 79)
		self._button1.TabIndex = 1
		self._button1.Text = "Calculate"
		self._button1.UseVisualStyleBackColor = True
		self._button1.Click += self.Button1Click
		# 
		# label2
		# 
		self._label2.BackColor = System.Drawing.Color.Chocolate
		self._label2.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label2.Location = System.Drawing.Point(27, 116)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(153, 49)
		self._label2.TabIndex = 2
		self._label2.Text = "Pay periods per year:"
		# 
		# label3
		# 
		self._label3.BackColor = System.Drawing.Color.Chocolate
		self._label3.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label3.Location = System.Drawing.Point(27, 195)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(153, 49)
		self._label3.TabIndex = 3
		self._label3.Text = "Salary per pay period:"
		# 
		# label4
		# 
		self._label4.BackColor = System.Drawing.Color.Chocolate
		self._label4.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label4.Location = System.Drawing.Point(253, 195)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(153, 49)
		self._label4.TabIndex = 4
		# 
		# textBox1
		# 
		self._textBox1.Location = System.Drawing.Point(253, 36)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(153, 20)
		self._textBox1.TabIndex = 5
		# 
		# textBox2
		# 
		self._textBox2.Location = System.Drawing.Point(253, 116)
		self._textBox2.Name = "textBox2"
		self._textBox2.Size = System.Drawing.Size(153, 20)
		self._textBox2.TabIndex = 6
		# 
		# MainForm
		# 
		self.ClientSize = System.Drawing.Size(465, 401)
		self.Controls.Add(self._textBox2)
		self.Controls.Add(self._textBox1)
		self.Controls.Add(self._label4)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._label1)
		self.Name = "MainForm"
		self.Text = "Salary Calculator"
		self.ResumeLayout(False)
		self.PerformLayout()


	def Button1Click(self, sender, e):
		a = int(self._textBox1.Text)
		b = int(self._textBox2.Text)
		c = str(round(a / b, 5))
		self._label4.Text = c
		