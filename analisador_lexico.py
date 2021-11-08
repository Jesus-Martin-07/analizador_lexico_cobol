import ply.lex as lex
import sys


reserved = {
    'ACCEPT': 'ACCEPT',
    'IDENTIFICATION' : 'IDENTIFICATION',
    'DIVISION' : 'DIVISION',
    'DATA' : 'DATA',
    'PROGRAM' : 'PROGRAM',
    'ID' : 'ID',
    'DATA' : 'DATA',
    'FILE' : 'FILE',
    'SECTION' : 'SECTION',
    'WORKING' : 'WORKING',
    'STORAGE' : 'STORAGE',
    'PIC' : 'PIC',
    'PROCEDURE' : 'PROCEDURE',
    'PERFORM' : 'PERFORM',
    'WITH' : 'WITH',
    'TEST' : 'TEST',
    'AFTER' : 'AFTER',
    'UNTIL' : 'UNTIL',
    'DISPLAY' : 'DISPLAY',
    'INICIO' : 'INICIO',
    'ACCEPT' : 'ACCEPT',
    'IF' : 'IF',
    'COMPUTE' : 'COMPUTE',
    'ELSE' : 'ELSE',
    'END' : 'END',
    'STOP' : 'STOP',
    'RUN' : 'RUN',
    'ALL' : 'ALL',
    'ALPHABET' : 'ALPHABET',
    'ALPHABETIC' : 'ALPHABETIC',
    'BINARY' : 'BINARY',
    'BLANK' : 'BLANK',
    'BLINK' : 'BLINK',
    'CALL' : 'CALL',
    'CANCEL' : 'CANCEL',
    'CD' : 'CD',
    'CONSOLEX' : 'CONSOLEX',
    'CONTAINS' : 'CONTAINS',
    'CONTENT' : 'CONTENT',
    'DELETE' : 'DELETE',
    'DELIMITED' : 'DELIMITED',
    'DELIMITER' : 'DELIMITER',
    'FILLER' : 'FILLER',
    'FINAL' : 'FINAL',
    'FIRST' : 'FIRST',
    'INDEXED' : 'INDEXED',
    'INDICATE' : 'INDICATE',
    'INITIAL' : 'INITIAL',
    'LEFT' : 'LEFT',
    'LEFTLINE' : 'LEFTLINE',
    'LENGTH' : 'LENGTH',
    'OFF' : 'OFF',
    'OMITTED' : 'OMITTED',
}

tokens = list(reserved.values())+[
    # Symbols
    'ASSIGN',
    'MOD',
    'PLUS',
    'PLUSPLUS',
    'PLUSEQUAL',
    'MINUS',
    'MINUSMINUS',
    'MINUSEQUAL',
    'TIMES',
    'DIVIDE',
    'LESS',
    'LESSEQUAL',
    'GREATER',
    'GREATEREQUAL',
    'EQUAL',
    'DEQUAL',
    'DISTINT',
    'ISEQUAL',
    'SEMICOLON',
    'COMMA',
    'LPAREN',
    'RPAREN',
    'LBRACKET',
    'RBRACKET',
    'LBLOCK',
    'RBLOCK',
    'COLON',
    'AMPERSANT',
    'HASHTAG',
    'DOT',
    'QUESTIONMARK',
    'COMILLASIMPLE',
    'COMILLASDOBLES',

    #variables
    'DOLLAR',

    # Others   
    'VARIABLE', 
    'VARIABLE2', 
    'NUMBER',
    'CADENA1',
    'CADENA2',
    'ID',
]

# Regular expressions rules for simple tokens
t_MOD = r'%'
t_PLUS   = r'\+'
t_MINUS  = r'-'
t_TIMES  = r'\*'
t_DIVIDE = r'/'
t_EQUAL  = r'='
t_DISTINT = r'!'
t_LESS   = r'<'
t_GREATER = r'>'
t_SEMICOLON = ';'
t_COMMA  = r','
t_LPAREN = r'\('
t_RPAREN  = r'\)'
t_LBRACKET = r'\['
t_RBRACKET = r'\]'
t_LBLOCK   = r'{'
t_RBLOCK   = r'}'
t_COLON   = r':'
t_AMPERSANT = r'\&'
t_HASHTAG = r'\#'
t_DOT = r'\.'
t_COMILLASIMPLE = r'\''
t_COMILLASDOBLES = r'\"'
t_QUESTIONMARK = r'\?'
t_DOLLAR = r'\$'
 
def t_NUMBER(t):
    r'\d+(\.\d+)?'
    t.value = float(t.value)
    return t

def t_VARIABLE(t):
    r'\$[a-zA-Z]([\w])*'
    return t

def t_VARIABLE2(t):
    r'[a-zA-Z](\w)*'
    if t.value in reserved:
        t.type = reserved[t.value]  # Check for reserved words
        return t
    else:
        return t

# Check reserved words
# This approach greatly reduces the number of regular expression rules and is likely to make things a little faster.
def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    if t.value in reserved:
        t.type = reserved[t.value]  # Check for reserved words
        return t
    else:
        t_error(t)

def t_CADENA1(t):
    r'\"([^\"].)*\"'
    return t

def t_CADENA2(t):
    r'\'([^\'].)*\''
    return t

def t_LESSEQUAL(t):
	r'<='
	return t

def t_GREATEREQUAL(t):
	r'>='
	return t

def t_ASSIGN(t):
    r'=>'
    return t

def t_DEQUAL(t):
	r'!='
	return t

def t_ISEQUAL(t):
	r'=='
	return t
    
def t_MINUSMINUS(t):
	r'--'
	return t

def t_PLUSPLUS(t):
	r'\+\+'
	return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_space(t):
    r'\s+'
    t.lexer.lineno += len(t.value)

t_ignore = ' \t'

def t_comments(t):
    r'/\*(.|\n)*?\*/'
    t.lexer.lineno += t.value.count('\n')

def t_comments_C99(t):
    r'//(.)*?\n'
    t.lexer.lineno += 1

def t_error(t):
    print ("Lexical error: " + str(t.value))
    t.lexer.skip(1)
    
def test(data, lexer):
	lexer.input(data)
	i = 1 #Representa la línea
	while True:     
		tok = lexer.token()
		if not tok:
			break
		print ("\t"+str(i)+" - "+"Line: "+str(tok.lineno)+"\t"+str(tok.type)+"\t-->  "+str(tok.value))
		i += 1
		#print(tok)


lexer = lex.lex()

 
if __name__ == '__main__':
	if (len(sys.argv) > 1):
		fin = sys.argv[1]
	else:
		fin = 'index.cbl'
	f = open(fin, 'r')
	data = f.read()
	print (data)
	lexer.input(data)
	test(data, lexer)
	input()