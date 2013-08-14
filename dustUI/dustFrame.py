#!/usr/bin/python

import sys
import os
if __name__ == '__main__':
    temp_path = sys.path[0]
    sys.path.insert(0, os.path.join(temp_path, '..', 'SmartMeshSDK'))

import Tkinter
import dustGuiLib
from dustStyle import dustStyle

from ApiException import CommandError
from ApiDefinition import ApiDefinition

class AutoHideScrollbar(Tkinter.Scrollbar):
    def set(self, lo, hi):
        if float(lo) <= 0.0 and float(hi) >= 1.0:
            self.tk.call("grid", "remove", self)
        else:
            self.grid()
        Tkinter.Scrollbar.set(self, lo, hi)

class dustFrame(Tkinter.Frame):
    '''
    \ingroup guiLib
    
    \brief A Tkinter frame with a Dust look-and-feel.
    '''
    
    MAX_HEIGHT      = 400
    MAX_WIDTH       = 900
    SIZE_REFRESH_MS = 500
    
    def __init__(self,parentElem,guiLock,frameName,row=0,column=0,scrollable=False):
    
        # record variables
        self.guiLock    = guiLock
        self.row        = row
        self.column     = column
        self.scrollable = scrollable
        
        # init parent
        Tkinter.Frame.__init__(self,parentElem,
                                    relief=Tkinter.SUNKEN,
                                    borderwidth=1,
                                    bg=dustStyle.COLOR_BG)
        
        #===
        
        # label
        temp = dustGuiLib.Label(self,
                             font=dustStyle.FONT_HEADER,
                             text=frameName,
                             bg=dustStyle.COLOR_BG)
        temp.grid(row=0,column=0,columnspan=2,sticky=Tkinter.W)
        
        #===
        
        # pad frame
        temp = Tkinter.Frame(self,bg=dustStyle.COLOR_BG,
                                  relief=Tkinter.FLAT)
        temp.grid(row=1,column=0,padx=10,pady=10)
        
        
        # container
        
        if self.scrollable:
            # the container is a frame with scrollbars which appear when 
            # it gets higher/wider than MAX_HEIGHT/MAX_WIDTH. 
            
            self.containerFrame = Tkinter.Frame(self,
                                                bg=dustStyle.COLOR_BG,
                                                relief=Tkinter.FLAT)
            self.containerFrame.grid(row=1,column=1,padx=5,pady=5)
            
            vscrollbar = AutoHideScrollbar(self.containerFrame, orient=Tkinter.VERTICAL)
            vscrollbar.grid(row=0, column=1, sticky=Tkinter.N+Tkinter.S)
            hscrollbar = AutoHideScrollbar(self.containerFrame, orient=Tkinter.HORIZONTAL)
            hscrollbar.grid(row=1, column=0, sticky=Tkinter.E+Tkinter.W)

            self.containerCanvas = Tkinter.Canvas(self.containerFrame,
                                                  width=100,
                                                  height=100,
                                                  borderwidth=0,
                                                  highlightthickness=0,
                                                  yscrollcommand=vscrollbar.set,
                                                  xscrollcommand=hscrollbar.set)
            self.containerCanvas.grid(row=0,
                                      column=0,
                                      sticky=Tkinter.N+Tkinter.S+Tkinter.E+Tkinter.W)

            vscrollbar.config(command=self.containerCanvas.yview)
            hscrollbar.config(command=self.containerCanvas.xview)

            # make the canvas expandable
            self.containerFrame.grid_rowconfigure(0, weight=1)
            self.containerFrame.grid_columnconfigure(0, weight=1)
            
            # create canvas contents
            self.container = Tkinter.Frame(self.containerCanvas,
                                           bg=dustStyle.COLOR_BG,
                                           padx=0,
                                           pady=0,
                                           border=0,
                                           relief=Tkinter.FLAT)
            
            self.containerCanvas.create_window(0,
                                               0,
                                               anchor=Tkinter.NW,
                                               window=self.container)
           
            self.container.update_idletasks()
            
            self._adjustCanvasSize()
        
        else:
            
            self.container = Tkinter.Frame(self,bg=dustStyle.COLOR_BG,
                                           relief=Tkinter.FLAT)
            self.container.grid(row=1,column=1,padx=5,pady=5)
        
        # local vars
        self.apiDef       = None
        self.connector    = None
        self.rowCtr       = 0
        self.colCtr       = 0
        self.guiElems     = []
        self.headerColor  = dustStyle.COLOR_PRIMARY2_LIGHT
                  
    #======================== public ==========================================
    
    def show(self):
        self.grid(row=self.row,
                  column=self.column,
                  sticky=Tkinter.N+Tkinter.E+Tkinter.S+Tkinter.W)
    
    def hide(self):
        self.grid_forget()
    
    def apiLoaded(self,apiDef):
        self.apiDef = apiDef
    
    def connectorLoaded(self,connector):
        self.connector = connector
    
    #======================== private =========================================
    
    def _add(self,elem,row,column,columnspan=1,sticky=Tkinter.W+Tkinter.E):
        try:
            elem.configure(font=dustStyle.FONT_BODY)
        except Tkinter.TclError:
            pass
        try:
            elem.configure(bg=dustStyle.COLOR_BG)
        except Tkinter.TclError:
            pass
        elem.grid(row=row,column=column,
                          columnspan=columnspan,
                          sticky=sticky)
    
    def _getHeaderColor(self):
        
        # toggle the color
        if self.headerColor==dustStyle.COLOR_PRIMARY2_LIGHT:
            self.headerColor = dustStyle.COLOR_PRIMARY2
        else:
            self.headerColor = dustStyle.COLOR_PRIMARY2_LIGHT
            
        # return the current color
        return self.headerColor
    
    def _clearGuiElems(self,level=0):
        '''
        \brief Clear all the GUI elements which are part of the list of GUI
               elements.
        
        \param elems The list of GUI elements. Valid values are:
                     - requestElems
                     - responseElems
                     - notifElems
        \param level The command level from which to start clearing (used for
                     clearing only subcommands). If 0, clears all elements.
        '''
        for c in self.guiElems[level:]:
            c['commandName']        = None,
            c['fieldNames']         = [],
            for elem in c['fieldNamesGui']:
                self.guiLock.acquire()
                elem.grid_forget()
                self.guiLock.release()
            c['fieldNamesGui']      = [],
            c['fieldFormats']       = [],
            for elem in c['fieldFormatsGui']:
                self.guiLock.acquire()
                elem.grid_forget()
                self.guiLock.release()
            c['fieldFormatsGui']    = [],
            c['fieldLengths']       = [],
            c['fieldOptions']       = [],
            for elem in c['fieldValuesGui']:
                self.guiLock.acquire()
                elem.grid_forget()
                self.guiLock.release()
            c['fieldValuesGui']     = [],
            c['fieldValuesString']  = [],
            c['fieldValuesRaw']     = [],
            c['fieldValues']        = [],
            if c['commandORbuttonGui']:
                self.guiLock.acquire()
                c['commandORbuttonGui'].grid_forget()
                self.guiLock.release()
            c['commandORbuttonGui'] = None,
        
        while len(self.guiElems)>level:
            self.guiElems.pop()
    
    def _adjustCanvasSize(self):
        
        frameHeight = self.container.winfo_reqheight()
        frameWidth  = self.container.winfo_reqwidth()
        
        self.containerCanvas.configure(height=min(frameHeight,self.MAX_HEIGHT))
        self.containerCanvas.configure(width =min(frameWidth, self.MAX_WIDTH) )
        
        self.container.rowconfigure(1, weight=1)
        self.container.columnconfigure(1, weight=1)
        self.containerCanvas.config(scrollregion=self.containerCanvas.bbox("all"))
        self.container.update_idletasks()
        
        # schedule to refresh the size in SIZE_REFRESH_MS ms
        self.after(self.SIZE_REFRESH_MS,self._adjustCanvasSize)
    
    #======================== helpers =========================================
    
    def _hexdata2string(self,array,start,stop):
        '''
        \brief Convert an array into a string.
        
        \param [in] array The array of bytes to convert, e.g. [0x01, 0x02]
        \param [in] start The index in the array from which to start
        \param [in] stop  The index in the array at which to stop
        
        \returns A string, e.g. '0102'
        '''
        output = ''
        for i in range(start,stop):
            temp = hex(array[i])[2:]
            if len(temp)==1:
                temp = '0'+temp
            output += temp
        return output

    def _hexdata2num(self,array,start,stop):
        '''
        \brief Convert an array into a number.
        
        \param [in] array The array of bytes to convert, e.g. [0x01, 0x02]
        \param [in] start The index in the array from which to start
        \param [in] stop  The index in the array at which to stop
        
        \returns A number, e.g. 0x0102 (or 258 in decimal)
        '''
        output = 0
        for i in range(start,stop):
            output += array[i]<<(8*(stop-i-1))
        return output

#============================ sample app ======================================
# The following gets called only if you run this module as a standalone app, by
# double-clicking on this source file. This code is NOT executed when importing
# this module is a larger application
#
class exampleApp(object):
    
    def __init__(self):
        self.window  = dustWindow("dustFrame",
                                  self._closeCb)
        self.guiLock            = threading.Lock()
        self.frame = dustFrame(self.window,
                               self.guiLock,
                               'dustFrame',
                               row=0,column=0)
        self.frame.show()
        self.window.mainloop()
    
    def _closeCb(self):
        print " _closeCb called"

if __name__ == '__main__':
    import threading
    from dustWindow import dustWindow
    exampleApp()
