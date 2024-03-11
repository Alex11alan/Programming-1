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
		self._label1 = System.Windows.Forms.Label()
		self._label2 = System.Windows.Forms.Label()
		self._label3 = System.Windows.Forms.Label()
		self._label4 = System.Windows.Forms.Label()
		self._label5 = System.Windows.Forms.Label()
		self._label6 = System.Windows.Forms.Label()
		self._label7 = System.Windows.Forms.Label()
		self._label8 = System.Windows.Forms.Label()
		self.SuspendLayout()
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.Color.Wheat
		self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 27.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.Location = System.Drawing.Point(12, 358)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(128, 71)
		self._button1.TabIndex = 0
		self._button1.Text = "Clear"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.Color.Wheat
		self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 27.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button2.Location = System.Drawing.Point(146, 358)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(203, 71)
		self._button2.TabIndex = 2
		self._button2.Text = "Calculate"
		self._button2.UseVisualStyleBackColor = False
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.BackColor = System.Drawing.Color.Wheat
		self._button3.Font = System.Drawing.Font("Microsoft Sans Serif", 27.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button3.Location = System.Drawing.Point(355, 358)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(128, 71)
		self._button3.TabIndex = 3
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = False
		self._button3.Click += self.Button3Click
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.Color.OldLace
		self._label1.Location = System.Drawing.Point(40, 33)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(226, 23)
		self._label1.TabIndex = 4
		self._label1.Text = "  "
		# 
		# label2
		# 
		self._label2.BackColor = System.Drawing.Color.OldLace
		self._label2.Location = System.Drawing.Point(40, 65)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(226, 23)
		self._label2.TabIndex = 5
		self._label2.Text = "  "
		# 
		# label3
		# 
		self._label3.BackColor = System.Drawing.Color.OldLace
		self._label3.Location = System.Drawing.Point(40, 100)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(226, 23)
		self._label3.TabIndex = 6
		self._label3.Text = "  "
		# 
		# label4
		# 
		self._label4.BackColor = System.Drawing.Color.OldLace
		self._label4.Location = System.Drawing.Point(40, 136)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(226, 23)
		self._label4.TabIndex = 7
		self._label4.Text = "  "
		# 
		# label5
		# 
		self._label5.BackColor = System.Drawing.Color.OldLace
		self._label5.Location = System.Drawing.Point(40, 172)
		self._label5.Name = "label5"
		self._label5.Size = System.Drawing.Size(226, 23)
		self._label5.TabIndex = 8
		self._label5.Text = "  "
		# 
		# label6
		# 
		self._label6.BackColor = System.Drawing.Color.OldLace
		self._label6.Location = System.Drawing.Point(40, 209)
		self._label6.Name = "label6"
		self._label6.Size = System.Drawing.Size(226, 23)
		self._label6.TabIndex = 9
		self._label6.Text = "  "
		# 
		# label7
		# 
		self._label7.BackColor = System.Drawing.Color.OldLace
		self._label7.Location = System.Drawing.Point(40, 246)
		self._label7.Name = "label7"
		self._label7.Size = System.Drawing.Size(226, 23)
		self._label7.TabIndex = 10
		self._label7.Text = "  "
		# 
		# label8
		# 
		self._label8.BackColor = System.Drawing.Color.OldLace
		self._label8.Location = System.Drawing.Point(40, 284)
		self._label8.Name = "label8"
		self._label8.Size = System.Drawing.Size(226, 23)
		self._label8.TabIndex = 11
		self._label8.Text = "  "
		# 
		# MainForm
		# 
		self.ClientSize = System.Drawing.Size(495, 441)
		self.Controls.Add(self._label8)
		self.Controls.Add(self._label7)
		self.Controls.Add(self._label6)
		self.Controls.Add(self._label5)
		self.Controls.Add(self._label4)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._label1)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Name = "MainForm"
		self.Text = "Schedule"
		self.ResumeLayout(False)

	def Button1Click(self, sender, e):
		self._label1.Text = ""
		self._label2.Text = ""
		self._label3.Text = ""
		self._label4.Text = ""
		self._label5.Text = ""
		self._label6.Text = ""
		self._label7.Text = ""
		self._label8.Text = ""

	def Button2Click(self, sender, e):
		self._label1.Text = "AP U.S. History"
		self._label2.Text = "English 11 Honor"
		self._label3.Text = "Computer Programming 1"
		self._label4.Text = "Chemistry Honor"
		self._label5.Text = "French II"
		self._label6.Text = "Power Chords"
		self._label7.Text = "Geometry Honor"
		self._label8.Text = "Health"

	def Button3Click(self, sender, e):
		Application.Exit()