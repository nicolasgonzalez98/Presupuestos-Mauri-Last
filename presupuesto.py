###########Librerias#############
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4, letter
import time
import os

#####Funciones###########
def validar(dato):
    while True:
        if dato:
            return dato
        else:
            print('No ingreso nada')
            print()
        dato=input('Ingrese de nuevo el dato: ')

def validarApel(dato):
	if dato=='':
		return ''

def convertir(dato):
	while True:
		try:
			dato=int(dato)
			return dato
		except ValueError:
			try:
				dato=float(dato)
				return dato
			except ValueError:
				print('Ingresaste un dato erroneo')
				print()
		dato=input('Ingrese un dato nuevamente: ')

def validarString(dato):
	while True:
		try:
			dato=int(dato)
			print('Ingreso un dato incorrecto.')
			dato=input('Intentelo nuevamente: ')
		except ValueError:
			return dato	

def ingresoNumPresupuesto():
	numPresupuesto=input('Ingrese el numero de presupuesto: ')
	numPresupuesto=validar(numPresupuesto)
	numPresupuesto=convertir(numPresupuesto)
	return numPresupuesto

def textoPresupuesto(numPresupuesto):
	presupuesto='PRESUPUESTO   #   '+str(numPresupuesto)
	textPres = c.beginText(200, 790)
	textPres.setFont(fuente, 15)
	textPres.textLine(presupuesto)
	c.drawText(textPres)
	

def nombreArchivo(numPresupuesto):
	direct=os.getcwd()
	direct+=" \Presupuestos-PDF\ "
	direct=direct.replace(' ','')
	if os.path.exists(direct)==False:
		os.mkdir(direct)
	numPresupuesto=str(numPresupuesto)+'.pdf'
	nomArch=direct+numPresupuesto
	return nomArch
	
def logo():
	email='E-Mail de contacto: info.ventas.decorglass@gmail.com'
	c.drawImage("decorglass.jpg", 20, 700, width=150, height=150)
	#E-Mail
	textEmail=c.beginText(w-315,720)
	textEmail.setFont(fuente,12)
	textEmail.textLine(email)
	c.drawText(textEmail)
	

def fecha():
	named_tuple = time.localtime() 
	time_string = time.strftime("%d/%m/%Y   %H:%M", named_tuple)

	textDate=c.beginText(470,700)
	textDate.setFont(fuente,12)
	textDate.textLine(time_string)
	c.drawText(textDate)

	#textHour=c.beginText(500,700)
	#textHour.setFont(fuente,12)
	#textHour.textLine(hour)
	#c.drawText(textHour)
	
def datoCliente():
	nroCliente=input('Ingrese numero cliente: ')
	nroCliente=validar(nroCliente)
	nroCliente=convertir(nroCliente)
	nomCliente=input('Ingrese el nombre del cliente: ')
	nomCliente=validar(nomCliente)
	nomCliente=validarString(nomCliente)
	nomCliente=nomCliente.upper()
	apelCliente=input('Ingrese el apellido del cliente: ')
	#apelCliente=validar(apelCliente)
	apelCliente=validarString(apelCliente)
	apelCliente=apelCliente.upper()
	name=apelCliente+' '+nomCliente
	cliente='CLIENTE: '+str(nroCliente)+'-'+name
	textCliente=c.beginText(20,700)
	textCliente.setFont(fuente,12)
	textCliente.textLine(cliente)
	c.drawText(textCliente)

def dibujarLinea(y):
	x = 20
	c.line(x, y, w-x, y)

def categorias():
	#CANTIDAD
	cantidadCat='Cantidad'
	textCantidadCat=c.beginText(30,h-170)
	textCantidadCat.setFont(fuente,12)
	textCantidadCat.textLine(cantidadCat)
	c.drawText(textCantidadCat)
	#DESCRIPCION
	descripcionCat='Descripción'
	textDescripcionCat=c.beginText(140,h-170)
	textDescripcionCat.setFont(fuente,12)
	textDescripcionCat.textLine(descripcionCat)
	c.drawText(textDescripcionCat)
	#MEDIDAS
	medidasCat='Medidas'
	textMedidasCat=c.beginText(w-330,h-170)
	textMedidasCat.setFont(fuente,12)
	textMedidasCat.textLine(medidasCat)
	c.drawText(textMedidasCat)
	#SUPERFICIE
	superficieCat='Superficie'
	textSuperficieCat=c.beginText(w-260,h-170)
	textSuperficieCat.setFont(fuente,12)
	textSuperficieCat.textLine(superficieCat)
	c.drawText(textSuperficieCat)
	#TOTAL UNIDAD
	uniCat='Precio por U.'
	textUniCat=c.beginText(w-190,h-170)
	textUniCat.setFont(fuente,12)
	textUniCat.textLine(uniCat)
	c.drawText(textUniCat)
	#TOTAL
	totalCat='Total'
	textTotalCat=c.beginText(w-60,h-170)
	textTotalCat.setFont(fuente,12)
	textTotalCat.textLine(totalCat)
	c.drawText(textTotalCat)
		
def limpiar():
	os.system('cls')

def agregarArticulos():
	articulos=[]
	categorias()
	limpiar()
	while True:
		print('1-Ingresar articulo')
		print('2-Crear PDF')
		print('3-Ver Informacion del programa')
		opc=input('Ingrese opcion: ')
		if opc=='1':
			nombre=input('Ingrese nombre del articulo: ')
			nombre=validar(nombre)
			cantidad=input(f'Ingrese cantidad de {nombre}: ')
			cantidad=validar(cantidad)
			cantidad=convertir(cantidad)
			ancho=input('Ingrese ancho: ')
			ancho=validar(ancho)
			ancho=convertir(ancho)
			alto=input('Ingrese alto: ')
			alto=validar(alto)
			alto=convertir(alto)
			sup=ancho*alto
			precio=input('Ingrese el precio por unidad: ')
			precio=validar(precio)
			precio=convertir(precio)
			total=precio*cantidad
			articulos.append((cantidad,nombre,ancho,alto,sup,precio,total))
		elif opc=='2':
			imprimirArticulos(articulos)
			break
		elif opc=='3':
			print()
			print('Programa desarrollado por Nicolas Nahuel Gonzalez.')
			print()
			print()
			print('CONTACTO')
			print()
			print('MAIL: nicolasgonzalez470@gmail.com')
			print()
			print()
		else:
			print('Ingresaste una opcion invalida')
		input("Toque ENTER para continuar...")
		os.system("cls")	
		
def imprimirArticulos(lista):
	precioTotal=0
	superficieTotal=0
	x=27
	y=h-200
	for i in range(len(lista)):
		cantidad,nombre,ancho,alto,sup,precio,total=lista[i]
		precioTotal+=total
		superficieTotal+=sup
		#CANTIDAD
		textCantT=c.beginText(x+10,y)
		textCantT.setFont(fuente,12)
		textCantT.textLine(str(cantidad))
		c.drawText(textCantT)
		#NOMBRE
		textNom=c.beginText(x+50,y)
		if len(nombre)<25:
			textNom.setFont(fuente,12)
		else:
			textNom.setFont(fuente,10)
		textNom.textLine(nombre)
		c.drawText(textNom)
		#MEDIDAS
		medida=f'{ancho} X {alto}'
		textMed=c.beginText(x+233,y)
		textMed.setFont(fuente,12)
		textMed.textLine(str(medida))
		c.drawText(textMed)
		#SUPERFICIE
		superficie=f'{sup}  M2'
		textSup=c.beginText(w-260,y)
		textSup.setFont(fuente,12)
		textSup.textLine(str(superficie))
		c.drawText(textSup)
		#PRECIO UNIDAD
		textPrec=c.beginText(w-160,y)
		textPrec.setFont(fuente,12)
		textPrec.textLine(str(precio))
		c.drawText(textPrec)
		#PRECIO TOTAL
		total=round(total,2)
		textPT=c.beginText(w-60,y)
		textPT.setFont(fuente,12)
		textPT.textLine(str(total))
		c.drawText(textPT)
		#Cambio
		y=y-20
	#Sup Total
	superficieTotal=str(superficieTotal)+' M2 '
	textSuperficie=c.beginText(w-260,y)
	textSuperficie.setFont(fuente,12)
	textSuperficie.textLine(superficieTotal)
	c.drawText(textSuperficie)
	#Barra
	y-=10
	dibujarLinea(y)
	#algo
	print()
	print()
	print('Desea cobrar el IVA?: ')
	print('1-Si')
	print('2-No')
	opc=input()
	print()
	print()
	precioTotal=round(precioTotal,2)
	while True:
		if opc=='1':
			totalIva=precioTotal*1.21
			totalIva=round(totalIva,2)
			IVA=precioTotal*0.21
			IVA=round(IVA,2)
			break
		elif opc=='2':
			totalIva=precioTotal
			IVA=0
			break
		else:
			print('Ingresaste una opcion invalida.')
		opc=input('Ingrese de nuevo su opcion sobre el IVA: ')
	#Label Precio TOTAL
	y-=15
	labelSubtotal='SUBTOTAL'
	textLSubt=c.beginText(w-250,y)
	textLSubt.setFont(fuente,12)
	textLSubt.textLine(labelSubtotal)
	c.drawText(textLSubt)
	#Precio TOTAL
	textTotalP=c.beginText(w-60,y)
	textTotalP.setFont(fuente,12)
	textTotalP.textLine(str(precioTotal))
	c.drawText(textTotalP)
	#Label TOTAL IVA
	y-=30
	labelIva='IVA'
	textImp=c.beginText(w-250,y)
	textImp.setFont(fuente,12)
	textImp.textLine(labelIva)
	c.drawText(textImp)
	#IVA
	precioConIva=str(IVA)
	textTotIva=c.beginText(w-60,y)
	textTotIva.setFont(fuente,12)
	textTotIva.textLine(precioConIva)
	c.drawText(textTotIva)
	#Label Precio Total con IVA
	y-=15
	labelTtlIva='TOTAL'
	textLabelImp=c.beginText(w-250,y)
	textLabelImp.setFont(fuente,12)
	textLabelImp.textLine(labelTtlIva)
	c.drawText(textLabelImp)
	#Precio con IVA
	textIva=c.beginText(w-60,y)
	textIva.setFont(fuente,12)
	textIva.textLine(str(totalIva))
	c.drawText(textIva)
	#Rectangulo
	y-=30
	rectangulo(y)
	texto_rectangulo(y)
	
def rectangulo(y):
	c.rect(25, y, 290, 80)
	
def texto_rectangulo(y):
	y+=71
	parr1='SR CLIENTE: El Presupuesto refleja el valor correspondiente al material solicitado con las'
	textParr1=c.beginText(27,y)
	textParr1.setFont(fuente,7)
	textParr1.textLine(parr1)
	c.drawText(textParr1)
	y-=10
	parr2='medidas provistas por usted o recomendadas por nuestros técnicos. Es IMPORTANTE que'
	textParr2=c.beginText(27,y)
	textParr2.setFont(fuente,7)
	textParr2.textLine(parr2)
	c.drawText(textParr2)
	y-=10
	parr3='revise el presupuesto ya que su aprobación es compromiso de producción del mismo.'
	textParr3=c.beginText(27,y)
	textParr3.setFont(fuente,7)
	textParr3.textLine(parr3)
	c.drawText(textParr3)
	y-=10
	parr4='La empresa no se hará responsable por diferencias que puedan producirse por este motivo.'
	textParr4=c.beginText(27,y)
	textParr4.setFont(fuente,7)
	textParr4.textLine(parr4)
	c.drawText(textParr4)
	y-=10
	parr5='Este presupuesto está sujeto a posibles aumentos. El precio definitivo de las mercaderías '
	textParr5=c.beginText(27,y)
	textParr5.setFont(fuente,7)
	textParr5.textLine(parr5)
	c.drawText(textParr5)
	y-=10
	parr6='presupuestadas se fijara en el momento de su efectivo pago.'
	textParr6=c.beginText(27,y)
	textParr6.setFont(fuente,7)
	textParr6.textLine(parr6)
	c.drawText(textParr6)
	
	
		
		
		
		
	
	
	
	
####Main#####
fuente='Helvetica'

while True:
	input('Pulse ENTER para iniciar el programa...')
	limpiar()
	numPresupuesto=ingresoNumPresupuesto()
	w, h = A4
	nomArch=nombreArchivo(numPresupuesto)
	c = canvas.Canvas(nomArch, pagesize=A4)
	logo()
	fecha()
	textoPresupuesto(numPresupuesto)
	datoCliente()
	dibujarLinea(h - 150)
	agregarArticulos()
	print()
	print()
	print(f'El archivo {numPresupuesto}.pdf fue crado satisfactoriamente.')
	print()
	input('Presione ENTER para finalizar...')
	
	c.save()
	break
	
	
	


