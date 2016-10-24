<Global.Microsoft.VisualBasic.CompilerServices.DesignerGenerated()>
Partial Class AwardGenerator
    Inherits System.Windows.Forms.Form

    'Form overrides dispose to clean up the component list.
    <System.Diagnostics.DebuggerNonUserCode()>
    Protected Overrides Sub Dispose(ByVal disposing As Boolean)
        Try
            If disposing AndAlso components IsNot Nothing Then
                components.Dispose()
            End If
        Finally
            MyBase.Dispose(disposing)
        End Try
    End Sub

    'Required by the Windows Form Designer
    Private components As System.ComponentModel.IContainer

    'NOTE: The following procedure is required by the Windows Form Designer
    'It can be modified using the Windows Form Designer.  
    'Do not modify it using the code editor.
    <System.Diagnostics.DebuggerStepThrough()>
    Private Sub InitializeComponent()
        Dim resources As System.ComponentModel.ComponentResourceManager = New System.ComponentModel.ComponentResourceManager(GetType(AwardGenerator))
        Me.OpenAsPrompt = New System.Windows.Forms.OpenFileDialog()
        Me.CSV_Ex_Trophy = New System.Windows.Forms.SaveFileDialog()
        Me.MenuStrip1 = New System.Windows.Forms.MenuStrip()
        Me.FileToolStripMenuItem = New System.Windows.Forms.ToolStripMenuItem()
        Me.OpenToolStripMenuItem = New System.Windows.Forms.ToolStripMenuItem()
        Me.AddFileToolStripMenuItem = New System.Windows.Forms.ToolStripMenuItem()
        Me.SaveToolStripMenuItem = New System.Windows.Forms.ToolStripMenuItem()
        Me.SaveAsToolStripMenuItem = New System.Windows.Forms.ToolStripMenuItem()
        Me.ExportToolStripMenuItem = New System.Windows.Forms.ToolStripMenuItem()
        Me.EditToolStripMenuItem = New System.Windows.Forms.ToolStripMenuItem()
        Me.AddToolStripMenuItem = New System.Windows.Forms.ToolStripMenuItem()
        Me.RemoveRowToolStripMenuItem = New System.Windows.Forms.ToolStripMenuItem()
        Me.HelpToolStripMenuItem = New System.Windows.Forms.ToolStripMenuItem()
        Me.KeyBindingsToolStripMenuItem = New System.Windows.Forms.ToolStripMenuItem()
        Me.TabPage1 = New System.Windows.Forms.TabPage()
        Me.Label2 = New System.Windows.Forms.Label()
        Me.PictureBox1 = New System.Windows.Forms.PictureBox()
        Me.TabAward = New System.Windows.Forms.TabPage()
        Me.ChangeRowButton = New System.Windows.Forms.Button()
        Me.FileInfo = New System.Windows.Forms.Button()
        Me.NumberAwards = New System.Windows.Forms.Label()
        Me.SetLimiters = New System.Windows.Forms.Button()
        Me.RemoveRow = New System.Windows.Forms.Button()
        Me.AddRow = New System.Windows.Forms.Button()
        Me.CSV_PATH = New System.Windows.Forms.Label()
        Me.DataTable = New System.Windows.Forms.DataGridView()
        Me.AwardType_COL = New System.Windows.Forms.DataGridViewTextBoxColumn()
        Me.Name_COL = New System.Windows.Forms.DataGridViewTextBoxColumn()
        Me.Year_COL = New System.Windows.Forms.DataGridViewTextBoxColumn()
        Me.TabControl1 = New System.Windows.Forms.TabControl()
        Me.SaveAsPrompt = New System.Windows.Forms.SaveFileDialog()
        Me.ExportAsPrompt = New System.Windows.Forms.SaveFileDialog()
        Me.OnlyTXTSave = New System.Windows.Forms.SaveFileDialog()
        Me.Label1 = New System.Windows.Forms.Label()
        Me.MenuStrip1.SuspendLayout()
        Me.TabPage1.SuspendLayout()
        CType(Me.PictureBox1, System.ComponentModel.ISupportInitialize).BeginInit()
        Me.TabAward.SuspendLayout()
        CType(Me.DataTable, System.ComponentModel.ISupportInitialize).BeginInit()
        Me.TabControl1.SuspendLayout()
        Me.SuspendLayout()
        '
        'OpenAsPrompt
        '
        Me.OpenAsPrompt.Filter = "txt/csv Files|*.csv;*.txt"
        '
        'CSV_Ex_Trophy
        '
        Me.CSV_Ex_Trophy.DefaultExt = "csv"
        Me.CSV_Ex_Trophy.FileName = ".csv"
        Me.CSV_Ex_Trophy.Filter = "CSV file|*.csv"
        '
        'MenuStrip1
        '
        Me.MenuStrip1.Items.AddRange(New System.Windows.Forms.ToolStripItem() {Me.FileToolStripMenuItem, Me.EditToolStripMenuItem, Me.HelpToolStripMenuItem})
        Me.MenuStrip1.Location = New System.Drawing.Point(0, 0)
        Me.MenuStrip1.Name = "MenuStrip1"
        Me.MenuStrip1.Size = New System.Drawing.Size(544, 24)
        Me.MenuStrip1.TabIndex = 3
        Me.MenuStrip1.Text = "MenuStrip1"
        '
        'FileToolStripMenuItem
        '
        Me.FileToolStripMenuItem.DropDownItems.AddRange(New System.Windows.Forms.ToolStripItem() {Me.OpenToolStripMenuItem, Me.AddFileToolStripMenuItem, Me.SaveToolStripMenuItem, Me.SaveAsToolStripMenuItem, Me.ExportToolStripMenuItem})
        Me.FileToolStripMenuItem.Name = "FileToolStripMenuItem"
        Me.FileToolStripMenuItem.Size = New System.Drawing.Size(37, 20)
        Me.FileToolStripMenuItem.Text = "File"
        '
        'OpenToolStripMenuItem
        '
        Me.OpenToolStripMenuItem.Name = "OpenToolStripMenuItem"
        Me.OpenToolStripMenuItem.Size = New System.Drawing.Size(213, 22)
        Me.OpenToolStripMenuItem.Text = "Open..              Ctrl-O"
        '
        'AddFileToolStripMenuItem
        '
        Me.AddFileToolStripMenuItem.Name = "AddFileToolStripMenuItem"
        Me.AddFileToolStripMenuItem.Size = New System.Drawing.Size(213, 22)
        Me.AddFileToolStripMenuItem.Text = "Add File To...   Ctrl-Shift-O"
        '
        'SaveToolStripMenuItem
        '
        Me.SaveToolStripMenuItem.Name = "SaveToolStripMenuItem"
        Me.SaveToolStripMenuItem.Size = New System.Drawing.Size(213, 22)
        Me.SaveToolStripMenuItem.Text = "Save                  Crtl-S"
        '
        'SaveAsToolStripMenuItem
        '
        Me.SaveAsToolStripMenuItem.Name = "SaveAsToolStripMenuItem"
        Me.SaveAsToolStripMenuItem.Size = New System.Drawing.Size(213, 22)
        Me.SaveAsToolStripMenuItem.Text = "Save As..           Ctrl-Shift-S"
        '
        'ExportToolStripMenuItem
        '
        Me.ExportToolStripMenuItem.Name = "ExportToolStripMenuItem"
        Me.ExportToolStripMenuItem.Size = New System.Drawing.Size(213, 22)
        Me.ExportToolStripMenuItem.Text = "Export As          Ctrl-E"
        '
        'EditToolStripMenuItem
        '
        Me.EditToolStripMenuItem.DropDownItems.AddRange(New System.Windows.Forms.ToolStripItem() {Me.AddToolStripMenuItem, Me.RemoveRowToolStripMenuItem})
        Me.EditToolStripMenuItem.Name = "EditToolStripMenuItem"
        Me.EditToolStripMenuItem.Size = New System.Drawing.Size(39, 20)
        Me.EditToolStripMenuItem.Text = "Edit"
        '
        'AddToolStripMenuItem
        '
        Me.AddToolStripMenuItem.Name = "AddToolStripMenuItem"
        Me.AddToolStripMenuItem.Size = New System.Drawing.Size(123, 22)
        Me.AddToolStripMenuItem.Text = "Add..."
        '
        'RemoveRowToolStripMenuItem
        '
        Me.RemoveRowToolStripMenuItem.Name = "RemoveRowToolStripMenuItem"
        Me.RemoveRowToolStripMenuItem.Size = New System.Drawing.Size(123, 22)
        Me.RemoveRowToolStripMenuItem.Text = "Remove.."
        '
        'HelpToolStripMenuItem
        '
        Me.HelpToolStripMenuItem.DropDownItems.AddRange(New System.Windows.Forms.ToolStripItem() {Me.KeyBindingsToolStripMenuItem})
        Me.HelpToolStripMenuItem.Name = "HelpToolStripMenuItem"
        Me.HelpToolStripMenuItem.Size = New System.Drawing.Size(44, 20)
        Me.HelpToolStripMenuItem.Text = "Help"
        '
        'KeyBindingsToolStripMenuItem
        '
        Me.KeyBindingsToolStripMenuItem.Name = "KeyBindingsToolStripMenuItem"
        Me.KeyBindingsToolStripMenuItem.Size = New System.Drawing.Size(142, 22)
        Me.KeyBindingsToolStripMenuItem.Text = "Key Bindings"
        '
        'TabPage1
        '
        Me.TabPage1.Controls.Add(Me.Label1)
        Me.TabPage1.Controls.Add(Me.Label2)
        Me.TabPage1.Controls.Add(Me.PictureBox1)
        Me.TabPage1.Location = New System.Drawing.Point(4, 22)
        Me.TabPage1.Name = "TabPage1"
        Me.TabPage1.Size = New System.Drawing.Size(449, 380)
        Me.TabPage1.TabIndex = 2
        Me.TabPage1.Text = "Credits"
        Me.TabPage1.UseVisualStyleBackColor = True
        '
        'Label2
        '
        Me.Label2.AutoSize = True
        Me.Label2.Location = New System.Drawing.Point(167, 74)
        Me.Label2.Name = "Label2"
        Me.Label2.Size = New System.Drawing.Size(88, 13)
        Me.Label2.TabIndex = 1
        Me.Label2.Text = "Some Other Stuff"
        '
        'PictureBox1
        '
        Me.PictureBox1.Image = CType(resources.GetObject("PictureBox1.Image"), System.Drawing.Image)
        Me.PictureBox1.Location = New System.Drawing.Point(194, 16)
        Me.PictureBox1.Name = "PictureBox1"
        Me.PictureBox1.Size = New System.Drawing.Size(32, 32)
        Me.PictureBox1.SizeMode = System.Windows.Forms.PictureBoxSizeMode.AutoSize
        Me.PictureBox1.TabIndex = 0
        Me.PictureBox1.TabStop = False
        '
        'TabAward
        '
        Me.TabAward.Controls.Add(Me.ChangeRowButton)
        Me.TabAward.Controls.Add(Me.FileInfo)
        Me.TabAward.Controls.Add(Me.NumberAwards)
        Me.TabAward.Controls.Add(Me.SetLimiters)
        Me.TabAward.Controls.Add(Me.RemoveRow)
        Me.TabAward.Controls.Add(Me.AddRow)
        Me.TabAward.Controls.Add(Me.CSV_PATH)
        Me.TabAward.Controls.Add(Me.DataTable)
        Me.TabAward.Location = New System.Drawing.Point(4, 22)
        Me.TabAward.Name = "TabAward"
        Me.TabAward.Padding = New System.Windows.Forms.Padding(3)
        Me.TabAward.Size = New System.Drawing.Size(449, 380)
        Me.TabAward.TabIndex = 0
        Me.TabAward.Text = "Awards"
        Me.TabAward.UseVisualStyleBackColor = True
        '
        'ChangeRowButton
        '
        Me.ChangeRowButton.Location = New System.Drawing.Point(187, 330)
        Me.ChangeRowButton.Name = "ChangeRowButton"
        Me.ChangeRowButton.Size = New System.Drawing.Size(75, 23)
        Me.ChangeRowButton.TabIndex = 16
        Me.ChangeRowButton.Text = "Edit..."
        Me.ChangeRowButton.UseVisualStyleBackColor = True
        '
        'FileInfo
        '
        Me.FileInfo.Location = New System.Drawing.Point(356, 9)
        Me.FileInfo.Name = "FileInfo"
        Me.FileInfo.Size = New System.Drawing.Size(75, 23)
        Me.FileInfo.TabIndex = 15
        Me.FileInfo.Text = "FileInfo"
        Me.FileInfo.UseVisualStyleBackColor = True
        '
        'NumberAwards
        '
        Me.NumberAwards.AutoSize = True
        Me.NumberAwards.Location = New System.Drawing.Point(22, 14)
        Me.NumberAwards.Name = "NumberAwards"
        Me.NumberAwards.Size = New System.Drawing.Size(84, 13)
        Me.NumberAwards.TabIndex = 13
        Me.NumberAwards.Text = "Number of Items"
        '
        'SetLimiters
        '
        Me.SetLimiters.Location = New System.Drawing.Point(309, 330)
        Me.SetLimiters.Name = "SetLimiters"
        Me.SetLimiters.Size = New System.Drawing.Size(104, 23)
        Me.SetLimiters.TabIndex = 11
        Me.SetLimiters.Text = "Set Limiters"
        Me.SetLimiters.UseVisualStyleBackColor = True
        '
        'RemoveRow
        '
        Me.RemoveRow.Location = New System.Drawing.Point(106, 330)
        Me.RemoveRow.Name = "RemoveRow"
        Me.RemoveRow.Size = New System.Drawing.Size(75, 23)
        Me.RemoveRow.TabIndex = 10
        Me.RemoveRow.Text = "Remove..."
        Me.RemoveRow.UseVisualStyleBackColor = True
        '
        'AddRow
        '
        Me.AddRow.Location = New System.Drawing.Point(25, 330)
        Me.AddRow.Name = "AddRow"
        Me.AddRow.Size = New System.Drawing.Size(75, 23)
        Me.AddRow.TabIndex = 9
        Me.AddRow.Text = "Add..."
        Me.AddRow.UseVisualStyleBackColor = True
        '
        'CSV_PATH
        '
        Me.CSV_PATH.AutoSize = True
        Me.CSV_PATH.Location = New System.Drawing.Point(235, 14)
        Me.CSV_PATH.Name = "CSV_PATH"
        Me.CSV_PATH.Size = New System.Drawing.Size(0, 13)
        Me.CSV_PATH.TabIndex = 8
        '
        'DataTable
        '
        Me.DataTable.AllowDrop = True
        Me.DataTable.AllowUserToAddRows = False
        Me.DataTable.AllowUserToDeleteRows = False
        Me.DataTable.AllowUserToResizeColumns = False
        Me.DataTable.AllowUserToResizeRows = False
        Me.DataTable.AutoSizeColumnsMode = System.Windows.Forms.DataGridViewAutoSizeColumnsMode.Fill
        Me.DataTable.ClipboardCopyMode = System.Windows.Forms.DataGridViewClipboardCopyMode.EnableWithoutHeaderText
        Me.DataTable.ColumnHeadersHeightSizeMode = System.Windows.Forms.DataGridViewColumnHeadersHeightSizeMode.AutoSize
        Me.DataTable.Columns.AddRange(New System.Windows.Forms.DataGridViewColumn() {Me.AwardType_COL, Me.Name_COL, Me.Year_COL})
        Me.DataTable.Location = New System.Drawing.Point(25, 48)
        Me.DataTable.Name = "DataTable"
        Me.DataTable.RowHeadersWidth = 30
        Me.DataTable.Size = New System.Drawing.Size(388, 276)
        Me.DataTable.TabIndex = 0
        '
        'AwardType_COL
        '
        Me.AwardType_COL.FillWeight = 30.0!
        Me.AwardType_COL.HeaderText = "AwardType"
        Me.AwardType_COL.Name = "AwardType_COL"
        '
        'Name_COL
        '
        Me.Name_COL.FillWeight = 50.0!
        Me.Name_COL.HeaderText = "Name"
        Me.Name_COL.Name = "Name_COL"
        '
        'Year_COL
        '
        Me.Year_COL.FillWeight = 20.0!
        Me.Year_COL.HeaderText = "Year"
        Me.Year_COL.Name = "Year_COL"
        '
        'TabControl1
        '
        Me.TabControl1.Controls.Add(Me.TabAward)
        Me.TabControl1.Controls.Add(Me.TabPage1)
        Me.TabControl1.Location = New System.Drawing.Point(46, 40)
        Me.TabControl1.Name = "TabControl1"
        Me.TabControl1.RightToLeft = System.Windows.Forms.RightToLeft.No
        Me.TabControl1.SelectedIndex = 0
        Me.TabControl1.Size = New System.Drawing.Size(457, 406)
        Me.TabControl1.TabIndex = 2
        '
        'SaveAsPrompt
        '
        Me.SaveAsPrompt.Filter = "TXT|*.txt|CSV|*.csv"
        '
        'ExportAsPrompt
        '
        Me.ExportAsPrompt.Filter = "DXF File|*.dxf"
        '
        'OnlyTXTSave
        '
        Me.OnlyTXTSave.Filter = "TXT|*.txt"
        '
        'Label1
        '
        Me.Label1.AutoSize = True
        Me.Label1.Location = New System.Drawing.Point(170, 131)
        Me.Label1.Name = "Label1"
        Me.Label1.Size = New System.Drawing.Size(39, 13)
        Me.Label1.TabIndex = 2
        Me.Label1.Text = "Label1"
        '
        'AwardGenerator
        '
        Me.AutoScaleDimensions = New System.Drawing.SizeF(6.0!, 13.0!)
        Me.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font
        Me.ClientSize = New System.Drawing.Size(544, 522)
        Me.Controls.Add(Me.TabControl1)
        Me.Controls.Add(Me.MenuStrip1)
        Me.KeyPreview = True
        Me.MainMenuStrip = Me.MenuStrip1
        Me.Name = "AwardGenerator"
        Me.Text = "AwardGenerator"
        Me.MenuStrip1.ResumeLayout(False)
        Me.MenuStrip1.PerformLayout()
        Me.TabPage1.ResumeLayout(False)
        Me.TabPage1.PerformLayout()
        CType(Me.PictureBox1, System.ComponentModel.ISupportInitialize).EndInit()
        Me.TabAward.ResumeLayout(False)
        Me.TabAward.PerformLayout()
        CType(Me.DataTable, System.ComponentModel.ISupportInitialize).EndInit()
        Me.TabControl1.ResumeLayout(False)
        Me.ResumeLayout(False)
        Me.PerformLayout()

    End Sub
    Friend WithEvents OpenAsPrompt As OpenFileDialog
    Friend WithEvents CSV_Ex_Trophy As SaveFileDialog
    Friend WithEvents MenuStrip1 As MenuStrip
    Friend WithEvents FileToolStripMenuItem As ToolStripMenuItem
    Friend WithEvents OpenToolStripMenuItem As ToolStripMenuItem
    Friend WithEvents SaveToolStripMenuItem As ToolStripMenuItem
    Friend WithEvents SaveAsToolStripMenuItem As ToolStripMenuItem
    Friend WithEvents ExportToolStripMenuItem As ToolStripMenuItem
    Friend WithEvents TabPage1 As TabPage
    Friend WithEvents Label2 As Label
    Friend WithEvents PictureBox1 As PictureBox
    Friend WithEvents TabAward As TabPage
    Friend WithEvents CSV_PATH As Label
    Friend WithEvents DataTable As DataGridView
    Friend WithEvents TabControl1 As TabControl
    Friend WithEvents AddRow As Button
    Friend WithEvents AwardType_COL As DataGridViewTextBoxColumn
    Friend WithEvents Name_COL As DataGridViewTextBoxColumn
    Friend WithEvents Year_COL As DataGridViewTextBoxColumn
    Friend WithEvents RemoveRow As Button
    Friend WithEvents AddFileToolStripMenuItem As ToolStripMenuItem
    Friend WithEvents SetLimiters As Button
    Friend WithEvents NumberAwards As Label
    Friend WithEvents SaveAsPrompt As SaveFileDialog
    Friend WithEvents FileInfo As Button
    Friend WithEvents ExportAsPrompt As SaveFileDialog
    Friend WithEvents ChangeRowButton As Button
    Friend WithEvents EditToolStripMenuItem As ToolStripMenuItem
    Friend WithEvents AddToolStripMenuItem As ToolStripMenuItem
    Friend WithEvents RemoveRowToolStripMenuItem As ToolStripMenuItem
    Friend WithEvents HelpToolStripMenuItem As ToolStripMenuItem
    Friend WithEvents KeyBindingsToolStripMenuItem As ToolStripMenuItem
    Friend WithEvents OnlyTXTSave As SaveFileDialog
    Friend WithEvents Label1 As Label
End Class
