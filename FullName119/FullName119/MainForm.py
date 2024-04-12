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
		self._button3 = System.Windows.Forms.Button()
		self._textBox1 = System.Windows.Forms.TextBox()
		self._textBox2 = System.Windows.Forms.TextBox()
		self._label1 = System.Windows.Forms.Label()
		self._label2 = System.Windows.Forms.Label()
		self._label3 = System.Windows.Forms.Label()
		self._label4 = System.Windows.Forms.Label()
		self.SuspendLayout()
		# 
		# button1
		# 
		self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.Location = System.Drawing.Point(12, 384)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(162, 142)
		self._button1.TabIndex = 0
		self._button1.Text = "Calculate"
		self._button1.UseVisualStyleBackColor = True
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button2.Location = System.Drawing.Point(180, 384)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(175, 142)
		self._button2.TabIndex = 1
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = True
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button3.Location = System.Drawing.Point(361, 384)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(162, 142)
		self._button3.TabIndex = 3
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = True
		self._button3.Click += self.Button3Click
		# 
		# textBox1
		# 
		self._textBox1.BackColor = System.Drawing.Color.MintCream
		self._textBox1.Location = System.Drawing.Point(291, 28)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(212, 20)
		self._textBox1.TabIndex = 4
		# 
		# textBox2
		# 
		self._textBox2.BackColor = System.Drawing.Color.MintCream
		self._textBox2.Location = System.Drawing.Point(291, 124)
		self._textBox2.Name = "textBox2"
		self._textBox2.Size = System.Drawing.Size(212, 20)
		self._textBox2.TabIndex = 5
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.Color.LightGreen
		self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label1.Location = System.Drawing.Point(52, 28)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(171, 74)
		self._label1.TabIndex = 6
		self._label1.Text = "First name:"
		# 
		# label2
		# 
		self._label2.BackColor = System.Drawing.Color.LightGreen
		self._label2.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label2.Location = System.Drawing.Point(52, 124)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(171, 74)
		self._label2.TabIndex = 7
		self._label2.Text = "Last name:"
		# 
		# label3
		# 
		self._label3.BackColor = System.Drawing.Color.LightGreen
		self._label3.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label3.Location = System.Drawing.Point(52, 218)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(171, 74)
		self._label3.TabIndex = 8
		self._label3.Text = "Your first and last name:"
		# 
		# label4
		# 
		self._label4.BackColor = System.Drawing.Color.LightGreen
		self._label4.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label4.Location = System.Drawing.Point(291, 218)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(212, 74)
		self._label4.TabIndex = 9
		# 
		# MainForm
		# 
		self.ClientSize = System.Drawing.Size(535, 538)
		self.Controls.Add(self._label4)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._label1)
		self.Controls.Add(self._textBox2)
		self.Controls.Add(self._textBox1)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Name = "MainForm"
		self.Text = "FullName119"
		self.ResumeLayout(False)
		self.PerformLayout()


	def Button1Click(self, sender, e):
		pass

	def Button2Click(self, sender, e):
		self._textBox1.Text = ""
		self._textBox2.Text = ""
		self._label4.Text = ""

	def Button3Click(self, sender, e):
		pass
	
	
	
	