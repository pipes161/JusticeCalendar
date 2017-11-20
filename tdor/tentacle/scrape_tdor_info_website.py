'''
Created on Nov 20, 2017

@author: Brian
'''
input = """
<p><strong>Argentina</strong></p>
<hr>
<p>Sofía Mailén Santillán<br>
Mercedes, Argentina<br>
1-Dec-16<br>
Beaten to death</p>
<p>A. Villegas<br>
Quilmes, Argentina<br>
14-Jan-17<br>
Shot in the head</p>
<p>Cindy Crawford Revlon<br>
Buenos Aires, Argentina<br>
1-Jun-17<br>
Decapitated</p>
<p>Pamela Tabarez<br>
Rosario, Argentina<br>
25-Jul-17<br>
Shot multiple times</p>
<p>Eyelen<br>
Tucuman, Argentina<br>
18-Aug-17<br>
Beaten</p>
<p><strong>Brazil</strong></p>
<hr>
<p>Juninho da Mangueira<br>
Guarus, Brazil<br>
21-Nov-16<br>
Shot at least five times.</p>
<p>Paola Bracho<br>
Manaus, Brazil<br>
24-Nov-16<br>
Suffocated</p>
<p>Michele Rios<br>
Rio de Janeiro, Brazil<br>
26-Nov-16<br>
Cause unclear</p>
<p>Patricia Araujo not reported<br>
Sao Paulo, Brazil<br>
27-Nov-16<br>
Shot in the head and burned</p>
<p>Dandara<br>
Natal, Brazil<br>
28-Nov-16<br>
Shot in the head</p>
<p>Name unknown<br>
Joao Pessoa, Brazil<br>
2-Dec-16<br>
Asphyxiation</p>
<p>M. Dias Machado<br>
Pontal do Parana, Brazil<br>
3-Dec-16<br>
Shot at least three times</p>
<p>Will Rhillary Silva<br>
Viamao, Brazil<br>
7-Dec-16<br>
Shot</p>
<p>Name unknown<br>
Rio de Janeiro, Brazil<br>
7-Dec-16<br>
Shot</p>
<p>R. da Silva de Sá<br>
Maceio, Brazil<br>
10-Dec-16<br>
Shot in the head</p>
<p>G. Aquino de Godoy<br>
Curitiba, Brazil<br>
14-Dec-16<br>
Shot in the head</p>
<p>D. de Souza<br>
Campos, Brazil<br>
17-Dec-16<br>
Shot in the neck and back</p>
<p>J. R. T. Gomes<br>
Crato, Brazil<br>
18-Dec-16<br>
Stoned to death</p>
<p>Gabriel Gomes<br>
Goiania, Brazil<br>
21-Dec-16<br>
Shot multiple times at the same incident as F. Braz</p>
<p>F. Braz<br>
Goiania, Brazil<br>
21-Dec-16<br>
Shot multiple times at the same incident as Gabriel Gomes</p>
<p>Paula Raio Laser 50<br>
Fortaleza, Brazil<br>
23-Dec-16<br>
Shot</p>
<p>Jake Helen<br>
Contagem, Brazil<br>
31-Dec-16<br>
Shot five times</p>
<p>Flávia Victoria Lima<br>
Sorocaba, Brazil<br>
31-Dec-16<br>
Cause unclear</p>
<p>L. C. Marinho<br>
Nova Cruz, Brazil<br>
4-Jan-17<br>
Stabbed</p>
<p>W. H. Soares dos Santos 16<br>
Teresina, Brazil<br>
6-Jan-17<br>
Shot</p>
<p>Mierala da Silva<br>
Bauru, Brazil<br>
13-Jan-17<br>
Beaten</p>
<p>Moranguinho<br>
Paranangua, Brazil<br>
15-Jan-17<br>
Shot</p>
<p>Agatha Lios<br>
Brasilia, Brazil<br>
18-Jan-17<br>
Cause not reported</p>
<p>Sandra<br>
Rio de Janeiro, Brazil<br>
19-Jan-17<br>
shot</p>
<p>Lady Dyana<br>
Manaus, Brazil<br>
19-Jan-17<br>
Stabbed</p>
<p>J. A. dos Santos<br>
Itabaianinha, Brazil<br>
26-Jan-17<br>
Shot to death</p>
<p>Paola Oliveira<br>
Russas, Brazil<br>
30-Jan-17<br>
Stoned to death</p>
<p>Name unknown<br>
Recife, Brazil<br>
3-Feb-17<br>
Drowned; legs were tied down</p>
<p>Agatha Mont<br>
Itapevi, Brazil<br>
4-Feb-17<br>
Suffocated</p>
<p>Name unknown<br>
Guaruja, Brazil<br>
8-Feb-17<br>
Stoned to death</p>
<p>Dandara dos Santos<br>
Fortaleza, Brazil<br>
15-Feb-17<br>
Beaten and stoned to death by a mob</p>
<p>Name unknown<br>
Caçapava, Brazil<br>
17-Feb-17<br>
Shot to death</p>
<p>A. da Silva Maciel<br>
Distrito de São Sebastião, Brazil<br>
18-Feb-17<br>
Shot</p>
<p>Mirella de Castro<br>
Belo Horizonte, Brazil<br>
19-Feb-17<br>
Suffocated</p>
<p>Camila de Souza Magalhães<br>
Sao Gonçalo, Brazil<br>
25-Feb-17<br>
Beaten</p>
<p>Emanuelle Muniz<br>
Anapolis, Brazil<br>
26-Feb-17<br>
Stoned to death</p>
<p>Lorrane<br>
São Luiz, Brazil<br>
26-Feb-17<br>
Shot to death</p>
<p>Z. Marrocos<br>
Guarabira, Brazil<br>
28-Feb-17<br>
Stabbed to death</p>
<p>Michelly Garcia<br>
Pelotas, Brazil<br>
3-Mar-17<br>
Shot</p>
<p>Name unknown<br>
Goiania, Brazil<br>
6-Mar-17<br>
Shot</p>
<p>Rubi<br>
Luziania, Brazil<br>
6-Mar-17<br>
Shot</p>
<p>Sandra<br>
Laranjeiras do Sul, Brazil<br>
8-Mar-17<br>
Beaten</p>
<p>Jennifer Celia Henrique (Jenni)<br>
Florianopolis, Brazil<br>
10-Mar-17<br>
Beaten</p>
<p>Name unknown<br>
Cachoeirinha, Brazil<br>
12-Mar-17<br>
Burned to death</p>
<p>Lexia<br>
Santa Fe do Sul, Brazil<br>
13-Mar-17<br>
Stabbed</p>
<p>Camila Albuquerque<br>
Salvador, Brazil<br>
15-Mar-17<br>
Shot</p>
<p>Bruninha<br>
Ourinhos, Brazil<br>
16-Mar-17<br>
Stabbed</p>
<p>Paola<br>
Street Joao Candido do Camara, Brazil<br>
22-Mar-17<br>
Stabbed to death</p>
<p>Paulina<br>
Recife, Brazil<br>
23-Mar-17<br>
Shot multiple times</p>
<p>Uilca or Wilka<br>
Loteamento Luiz Gonzaga, Brazil.<br>
26-Mar-17<br>
Stabbed in the neck</p>
<p>Name unknown<br>
Acara, Brazil<br>
2-Apr-17<br>
Beaten</p>
<p>Name unknown<br>
Campo Grande, Brazil<br>
3-Apr-17<br>
Not reported</p>
<p>R. Félix da Silva<br>
Guarariba, Brazil<br>
4-Apr-17<br>
Shot to death</p>
<p>Bianka Gonçalves<br>
Primavera do Leste, Brazil<br>
7-Apr-17<br>
Shot to death</p>
<p>Camila<br>
Sao Jose do Campos, Brazil<br>
10-Apr-17<br>
Beaten</p>
<p>Vitoria Castro<br>
Araguaina, Brazil<br>
10-Apr-17<br>
Beaten</p>
<p>Hérica Izidório<br>
Fortaleza, Brazil<br>
12-Apr-17<br>
Beaten</p>
<p>Name unknown<br>
Curitiba, Brazil<br>
12-Apr-17<br>
Beaten</p>
<p>Gaby<br>
Feira de Santana, Brazil<br>
12-Apr-17<br>
Shot to death</p>
<p>Name unknown<br>
Itabuna, Brazil<br>
16-Apr-17<br>
Shot to death</p>
<p>Samilly Guimarães<br>
Rio de Janeiro, Brazil<br>
20-Apr-17<br>
Shot to death</p>
<p>Marooni<br>
Belem, Brazil<br>
22-Apr-17<br>
Stabbed to death</p>
<p>A. Ribeiro Marcossone<br>
Curitiba, Brazil<br>
23-Apr-17<br>
Shot over 25 times</p>
<p>Eloá Silva<br>
Joao Pessoa, Brazil<br>
27-Apr-17<br>
Shot multiple times</p>
<p>Name unknown<br>
Barcarena, Brazil<br>
29-Apr-17<br>
Stabbed</p>
<p>Uilca<br>
Vitoria de Santo Antao, Brazil<br>
29-Apr-17<br>
Shot to death</p>
<p>Layza Mello<br>
Vilha Velha, Brazil<br>
30-Apr-17<br>
Shot</p>
<p>Name unknown<br>
Belem, Brazil<br>
30-Apr-17<br>
Shot to death</p>
<p>Samaielly<br>
Lauro de Freitas, Brazil<br>
30-Apr-17<br>
Shot to death</p>
<p>Sophia Castro<br>
Contagem, Brazil<br>
3-May-17<br>
Cause unclear</p>
<p>C. A. Lima da Silva<br>
Monhangape, Brazil<br>
6-May-17<br>
Shot to death</p>
<p>R. C. Silva Pereira<br>
Barretos, Brazil<br>
7-May-17<br>
Deliberately struck by a vehicle</p>
<p>Thadeu Nascimento<br>
Grande do Retiro, Brazil<br>
7-May-17<br>
Shot and beaten</p>
<p>Jennifer<br>
Itaitinga, Brazil<br>
9-May-17<br>
Shot multiple times</p>
<p>Fernanda<br>
Ponta Grossa, Brazil<br>
10-May-17<br>
Shot</p>
<p>Chaiane<br>
Cachoeira do Sul, Brazil<br>
13-May-17<br>
Stabbed</p>
<p>Ketlin<br>
Juazeiro do Norte, Brazil<br>
13-May-17<br>
Stabbed</p>
<p>Name unknown<br>
Fortaleza, Brazil<br>
13-May-17<br>
Stabbed</p>
<p>Name unknown<br>
Morro Agudo, Brazil<br>
15-May-17<br>
Beaten to death</p>
<p>Pâmela<br>
Belo Horizonte, Brazil<br>
21-May-17<br>
Stabbed to death</p>
<p>Lalá<br>
Feira de Santana, Brazil<br>
25-May-17<br>
Shot to death</p>
<p>Grace Kelly<br>
Lauro de Freitas, Brazil<br>
25-May-17<br>
Suffocated</p>
<p>Joyce Jane Padilha<br>
Rio de Janeiro, Brazil<br>
26-May-17<br>
dismembered</p>
<p>Sheila Medeiros<br>
Tres Pontas, Brazil<br>
29-May-17<br>
Cause not reported</p>
<p>Laryrssa Moura<br>
Governador Valadares, Brazil<br>
31-May-17<br>
Shot in the back</p>
<p>Natasha<br>
Castanhal, Brazil<br>
5-Jun-17<br>
Multiple gunshot wounds</p>
<p>A. Alves Nascimento<br>
Criciúma, Brazil<br>
5-Jun-17<br>
Shot to death</p>
<p>Natasha<br>
Varginha, Brazil<br>
6-Jun-17<br>
Shot multiple times</p>
<p>Name unknown<br>
Salvador, Brazil<br>
10-Jun-17<br>
Shot in the neck, belly, shoulder, and back.</p>
<p>Renata Vieira<br>
Uberlândia, Brazil<br>
14-Jun-17<br>
Beaten to death</p>
<p>E. Shyne<br>
Rio de Janeiro, Brazil<br>
15-Jun-17<br>
Tortured</p>
<p>Julhão Petruk<br>
Fortaleza, Brazil<br>
15-Jun-17<br>
Shot multiple times</p>
<p>Name unknown<br>
Caraguatatuba, Brazil<br>
16-Jun-17<br>
Stabbed</p>
<p>Bárbara<br>
Maceió, Brazil<br>
18-Jun-17<br>
Struck by a vehicle</p>
<p>Name unknown<br>
Belo Horizonte, Brazil<br>
19-Jun-17<br>
Shot to death</p>
<p>Camily Victoria<br>
Belo Horizonte, Brazil<br>
22-Jun-17<br>
Shot to death</p>
<p>Denise<br>
Aracaju, Brazil<br>
24-Jun-17<br>
Shot to death</p>
<p>C. Barroso de Oliveira<br>
Ananindeua, Brazil<br>
24-Jun-17<br>
Shot to death</p>
<p>Nicolly Santos<br>
Vitória de Santo Antão, Brazil<br>
24-Jun-17<br>
Stabbed multiple times</p>
<p>Ney Oliveira<br>
Apuarema, Brazil<br>
25-Jun-17<br>
Stabbed to death</p>
<p>Salomé Bracho<br>
São Luís do Curu, Brazil<br>
25-Jun-17<br>
Shot to death</p>
<p>Tabata Brandão<br>
Rondonópolis, Brazil<br>
25-Jun-17<br>
Shot to death</p>
<p>Carla<br>
Maceió, Brazil<br>
28-Jun-17<br>
Stabbed to death</p>
<p>Lola<br>
Sorriso, Brazil<br>
2-Jul-17<br>
Cause not reported</p>
<p>Rayane<br>
Fortaleza, Brazil<br>
2-Jul-17<br>
Shot</p>
<p>Larissa<br>
Fortaleza, Brazil<br>
2-Jul-17<br>
Multiple gunshot wounds</p>
<p>Vicky Spears<br>
Diadema, Brazil<br>
3-Jul-17<br>
Shot</p>
<p>Anna Sophia<br>
João Pessoa, Brazil<br>
8-Jul-17<br>
Shot in the head</p>
<p>Bruna dos Santos<br>
Pelotas, Brazil<br>
9-Jul-17<br>
Beaten and shot</p>
<p>Cauã<br>
Porto Alegre, Brazil<br>
9-Jul-17<br>
Shot</p>
<p>Thalia<br>
Rio Verde, Brazil<br>
14-Jul-17<br>
Shot</p>
<p>Sophia<br>
Campo Mourão, Brazil<br>
17-Jul-17<br>
Stabbed to death</p>
<p>Michele<br>
Caxias, Brazil<br>
17-Jul-17<br>
Shot</p>
<p>Leona Albuquerque<br>
Salvador, Brazil<br>
17-Jul-17<br>
Shot multiple times</p>
<p>Camila Guedes<br>
Monte Mor, Brazil<br>
20-Jul-17<br>
Stabbed</p>
<p>Gil Pereia da Costa<br>
Rio Branco, Brazil<br>
20-Jul-17<br>
Shot twice</p>
<p>Gabriela Sousa<br>
Maracanaú, Brazil<br>
21-Jul-17<br>
Shot</p>
<p>E. A. da Silva<br>
Maceio, Brazil<br>
21-Jul-17<br>
Shot</p>
<p>Name unknown<br>
Belo Horizonte, Brazil<br>
22-Jul-17<br>
Stabbed to death</p>
<p>Natalia Pimentel<br>
Várzea Grande, Brazil<br>
25-Jul-17<br>
run over multiple times</p>
<p>Aurinete<br>
Patos do Piauí, Brazil<br>
31-Jul-17<br>
Stabbed</p>
<p>Name unknown<br>
João Pessoa, Brazil<br>
1-Aug-17<br>
Dragged and shot in the head.</p>
<p>Mary Monttila<br>
Palmeira dos Índios, Brazil<br>
2-Aug-17<br>
Stabbed on the neck.</p>
<p>Charliane<br>
Itabuna, Brazil<br>
2-Aug-17<br>
Shot</p>
<p>Bruna Laclose<br>
Pinheiro Machado, Brazil<br>
6-Aug-17<br>
Sstabbed</p>
<p>Paulinha<br>
Palmares, Brazil<br>
8-Aug-17<br>
Stabbed to death.</p>
<p>T. J. Gomes da Silva<br>
João Pessoa, Brazil<br>
12-Aug-17<br>
Multiple gunshot wounds</p>
<p>Dianna<br>
Limoeiro, Brazil<br>
18-Aug-17<br>
Shot</p>
<p>Evelin Ferrari<br>
Caruaru, Brazil<br>
22-Aug-17<br>
Shot</p>
<p>Lilly<br>
Cachoeira, Brazil<br>
27-Aug-17<br>
Shot to death</p>
<p>Daniele Jesus Lafon<br>
Poços de Caldas, Brazil<br>
2-Sep-17<br>
Stabbed with a pair of scissors</p>
<p>Flávia<br>
Santos, Brazil<br>
3-Sep-17<br>
Shot</p>
<p>Rai<br>
Petrolândia, Brazil<br>
3-Sep-17<br>
Stoned to death</p>
<p>Ana Carolina Nascimento<br>
Araraquara, Brazil<br>
5-Sep-17<br>
Beaten to deat</p>
<p>Nicole<br>
Sorriso, Brazil<br>
5-Sep-17<br>
Stabbed to death</p>
<p>Alessandra<br>
São Paulo, Brazil<br>
7-Sep-17<br>
Shot</p>
<p>Bruna Monteiro<br>
Taguatinga Sul, Brazil<br>
8-Sep-17<br>
Shot to death</p>
<p>Lorane<br>
Camocim de São Felix, Brazil<br>
9-Sep-17<br>
Shot</p>
<p>Larissa Paiva<br>
Serra, Brazil<br>
14-Sep-17<br>
Serra, Brazil</p>
<p>Safira<br>
Salvador, Brazil<br>
15-Sep-17<br>
Shot to death</p>
<p>Name unknown<br>
Camaçari, Brazil<br>
16-Sep-17<br>
Shot</p>
<p>Ana Coutti<br>
Cabo Frio, Brazil<br>
18-Sep-17<br>
MUltiple gunshot wounds</p>
<p>Kaleane<br>
Belo Horizonte, Brazil<br>
20-Sep-17<br>
Shot in the head</p>
<p>Spencer<br>
Campinas, Brazil<br>
23-Sep-17<br>
Beaten and stabbed</p>
<p>D.R.P.<br>
Campinas, Brazil<br>
24-Sep-17<br>
Stabbed to death</p>
<p>Pâmela<br>
Moreilândia, Brazil<br>
25-Sep-17<br>
Shot and beaten</p>
<p>Danhy Zn<br>
Leme, Brazil<br>
25-Sep-17<br>
Not specified</p>
<p>Rayssa<br>
Uberaba, Brazil<br>
26-Sep-17<br>
Shot twice</p>
<p>Lu Brasil<br>
Altamira, Brazil<br>
26-Sep-17<br>
Cut and strangled</p>
<p>Renatha Lemos<br>
Nova Mamoré, Brazil<br>
30-Sep-17<br>
Burned</p>
<p>Natália<br>
Fortaleza, Brazil<br>
30-Sep-17<br>
Shot</p>
<p><strong>Canada</strong></p>
<hr>
<p>Sisi Thibert<br>
Montreal, Quebec, Canada<br>
18-Sep-17<br>
Stabbed to death</p>
<p><strong>Chile</strong></p>
<hr>
<p>Vanessa Valenzuela<br>
Viña del Mar, Region Valparaiso, Chile<br>
28-Apr-17<br>
Beaten with hammers and sticks by five people who yelled “kill the fag.”</p>
<p><strong>Colombia</strong></p>
<hr>
<p>Alejandro Polanco Botero<br>
Risaralda, Colombia<br>
30-Nov-16<br>
Shot four times in the head</p>
<p>Vikichy<br>
Cali, Colombia<br>
20-Jan-17<br>
Stabbed in the chin and stomach</p>
<p>Silvana Fabian Pineda<br>
La Dorada, Colombia<br>
28-Jan-17<br>
Multiple gunshot wounds</p>
<p>Angelo Ramos<br>
Garzon, Colombia<br>
9-Feb-17<br>
Not reported</p>
<p>Name unknown<br>
Chaparral, Colombia<br>
16-Feb-17<br>
Beaten, and was violently sexually assaulted prior to death</p>
<p>C. Camilo Valencia<br>
Valle del Cauca, Colombia<br>
19-Feb-17<br>
Shot</p>
<p>Mafe Rojas Camilo<br>
Tolima, Colombia<br>
3-May-17<br>
Tortured, beaten, shot</p>
<p>Andrea Chaguendo Suárez<br>
Cali, Colombia<br>
31-May-17<br>
Stabbed</p>
<p>Juliana Orrego Monsalve<br>
Valle de Cauc, Colombia<br>
2-Jul-17<br>
Shot multiple times</p>
<p>Malvilis Trujillo<br>
Tolima, Colombia<br>
27-Aug-17<br>
Not reported</p>
<p><strong>Costa Rica</strong></p>
<hr>
<p>Kenicha<br>
Pococí, Costa Rica<br>
15-Aug-17<br>
Asphyxiation</p>
<p><strong>Dominican Republic</strong></p>
<hr>
<p>Jessica Rubi Mori<br>
La Romana, Dominican Republic<br>
3-Jun-17<br>
Dismembered</p>
<p>Carolina Alexis Zapata<br>
Santo Domingo, Dominican Republic<br>
22-Jul-17<br>
beat over the head with a stick</p>
<p><strong>Ecuador</strong></p>
<hr>
<p>W. Fabricio Ponce<br>
Banabi, Ecuador<br>
20-Dec-16<br>
Tortured and burned</p>
<p><strong>El Salvador</strong></p>
<hr>
<p>Name unknown<br>
San Salvador, El Salvador<br>
20-Nov-16<br>
Beaten to death</p>
<p>Name unknown<br>
San Salvador, El Salvador<br>
17-Jan-17<br>
Shot and thrown into the road</p>
<p>T. A. Orellana<br>
San Luis Talpa, El Salvador<br>
18-Feb-17<br>
Shot at the same time as D. Rodriguez</p>
<p>D. Rodriguez<br>
San Luis Talpa, El Salvador<br>
18-Feb-17<br>
Shot at the same time as T.A. Orellana</p>
<p>Elizabeth<br>
San Luis Talpa, El Salvador<br>
20-Feb-17<br>
Found with her hands and feet bound, with wounds to her face and neck.</p>
<p>Name unknown<br>
Ilopango, El Salvador<br>
20-May-17<br>
Shot to death</p>
<p>Misty<br>
Usulutan, El Salvador<br>
27-Aug-17<br>
Strangled</p>
<p><strong>Honduras</strong></p>
<hr>
<p>Sherlyn Montoya<br>
Tegucigalpa, Honduras<br>
4-Apr-17<br>
Tortured; her body was discovered in a bag</p>
<p>Tato Eduardo Ayestas<br>
El Paraíso, Honduras<br>
23-Apr-17<br>
Stabbed multiple times</p>
<p><strong>India</strong></p>
<hr>
<p>Vasu Swamy<br>
Bangalore, India<br>
16-Dec-16<br>
Cause not reported</p>
<p>Shama<br>
Tej Mohan Nagar, India<br>
30-Apr-17<br>
Stabbed</p>
<p>Kajal<br>
Patna, India<br>
29-Jul-17<br>
Throat slit</p>
<p><strong>Italy</strong></p>
<hr>
<p>Unnamed Transwoman<br>
Rome, Italy<br>
10-Nov-17<br>
Stabbed to death</p>
<p><strong>Malaysia</strong></p>
<hr>
<p>Meera<br>
Kuala Lumpur, Malaysia<br>
23-Feb-17<br>
Victim was shot and stabbed</p>
<p>Name unknown<br>
Flat Sri Plateau, Bandar Sri Permaisuri, Cheras, Malaysia<br>
5-May-17<br>
Exact cause not reported. Was found in her apartment, bound</p>
<p><strong>Mexico</strong></p>
<hr>
<p>Hannia Camacho Rodriguez<br>
Victoria, Mexico<br>
23-Nov-16<br>
Shot three times</p>
<p>Name unknown<br>
Sinaloa, Mexico<br>
1-Jan-17<br>
Cause unclear</p>
<p>Michelle de la Cruz González<br>
Coahuila, Mexico<br>
6-Jan-17<br>
Beaten with a hammer</p>
<p>Name unknown<br>
Guerrero, Mexico<br>
7-Jan-17<br>
Shot</p>
<p>J.C.N<br>
Estado de Mexico, Mexico<br>
11-Jan-17<br>
Shot 16 times</p>
<p>Name unknown<br>
Magdalena Contreras, Mexico<br>
14-Jan-17<br>
Stabbed</p>
<p>Anahí Tapia Llamas<br>
Guadalajara, Mexico<br>
18-Jan-17<br>
Two gunshot wounds. Victim was then thrown into the street</p>
<p>Name unknown<br>
Calimaya, Mexico<br>
1-Feb-17<br>
Multilated</p>
<p>Name unknown<br>
Municipio Centro, Mexico<br>
5-Feb-17<br>
Shot to death</p>
<p>Byanka Yañez<br>
Matamoros, Mexico<br>
24-Feb-17<br>
Stabbed</p>
<p>Name unknown<br>
Municipio de Chalco, Mexico<br>
1-Mar-17<br>
Stabbed</p>
<p>Name unknown<br>
Tlajomulco, Mexico<br>
1-Mar-17<br>
Cause unknown; body was found in an abandoned suitcase</p>
<p>H. Ramirez Calderon<br>
Guanajuato, Mexico<br>
20-Mar-17<br>
Shot multiple times</p>
<p>Paola<br>
Tamaulipas, Mexico<br>
20-Mar-17<br>
Beaten, her body was thrown in the street after she was killed</p>
<p>Yadira Lopez Marroquin<br>
Monterrey, Mexico<br>
16-Apr-17<br>
asphyxiated</p>
<p>Monse Morga Javier<br>
Guerrero, Mexico<br>
17-Apr-17<br>
Shot to death</p>
<p>Yadira López Marroquín<br>
Monterrey, Nuevo León, Mexico<br>
18-Apr-17<br>
Strangled</p>
<p>Name unknown<br>
Michoacan, Mexico<br>
4-May-17<br>
Stabbed to death</p>
<p>Ivanna Landuchy<br>
Tamaulipas, Mexico<br>
12-May-17<br>
Shot</p>
<p>Jennifer López<br>
Guerrero, Mexico<br>
20-May-17<br>
Stabbed to death</p>
<p>Caricia<br>
Guerrero, Mexico<br>
26-May-17<br>
Shot</p>
<p>Name unknown<br>
Guerrero, Mexico<br>
28-May-17<br>
stoned to death</p>
<p>Name unknown<br>
Puebla, Mexico<br>
1-Jun-17<br>
Exact cause not reported. Discovered bound with a bag over her head.</p>
<p>Fernanda/Tavita Montes<br>
Colima, Mexico<br>
4-Jun-17<br>
Asphyxiation</p>
<p>Denisse de León<br>
Ciudad Victoria, Mexico<br>
10-Jun-17<br>
Shot to death</p>
<p>Kenya<br>
Estado de Mexico, Mexico<br>
18-Jun-17<br>
Cause not reported</p>
<p>Adriana Cruz Serrano<br>
Veracruz, Mexico<br>
20-Jun-17<br>
Shot to death</p>
<p>Name unknown<br>
Sinaloa, Mexico<br>
1-Jul-17<br>
Shot</p>
<p>Name unknown<br>
Estado de Mexico, Mexico<br>
4-Jul-17<br>
Shot</p>
<p>Yadira Lopez Marroquin<br>
Puebla, Mexico<br>
6-Jul-17<br>
Stabbed</p>
<p>Claudia Muñoz García<br>
Altamirano, Mexico<br>
15-Jul-17<br>
Hit by a car</p>
<p>Name unknown<br>
Reynosa, Mexico<br>
17-Jul-17<br>
Beaten with a stone</p>
<p>Name unknown<br>
Nuevo Leon, Mexico<br>
27-Jul-17<br>
Shot to death</p>
<p>Name unknown<br>
Morelos, Mexico<br>
30-Jul-17<br>
Shot to death</p>
<p>La Chapopota<br>
Puebla, Mexico<br>
13-Aug-17<br>
Blunt force trauma to the head</p>
<p>Cristal<br>
Morelos, Mexico<br>
13-Aug-17<br>
Shot to death</p>
<p>Name unknown<br>
Morelos, Mexico<br>
20-Aug-17<br>
Multiple gunshot wounds</p>
<p>Name unknown<br>
Chihuahua, Mexico<br>
21-Aug-17<br>
Not specified</p>
<p>La Peluchina<br>
Colima, Mexico<br>
23-Aug-17<br>
Throat slit</p>
<p>Name unknown<br>
Acapulco, Mexico<br>
27-Aug-17<br>
Shot to death</p>
<p>Name unknown<br>
Durango, Mexico<br>
27-Aug-17<br>
Beaten</p>
<p>Name unknown<br>
Chihuahua, Mexico<br>
31-Aug-17<br>
not reported; discovered with a bag over her head</p>
<p>Mendez Cuevas<br>
Durango, Mexico<br>
1-Sep-17<br>
not reported</p>
<p>Name unknown<br>
Estado de Mexico, Mexico<br>
1-Sep-17<br>
Not specified</p>
<p>Manuela<br>
Fresnillo, Mexico<br>
3-Sep-17<br>
Stabbed in the neck with a screwdriver</p>
<p>Brenda Murillo Alba<br>
Baja California Norte, Mexico<br>
12-Sep-17<br>
Stabbed</p>
<p>Name unknown<br>
Chihuahua, Mexico<br>
19-Sep-17<br>
Shot to death</p>
<p><strong>The Netherlands</strong></p>
<hr>
<p>Bianca<br>
Arnhem, The Netherlands<br>
29-Sep-17<br>
Stabbed over twenty times</p>
<p><strong>Pakistan</strong></p>
<hr>
<p>Imli<br>
Lahore, Pakistan<br>
21-Jan-17<br>
Wrists slit, allegedly by her boyfriend</p>
<p>Muskan<br>
Lahore, Pakistan<br>
27-Jan-17<br>
Throat slit. Victim was also beatene</p>
<p>Sitara<br>
Sialkot, Pakistan<br>
9-Apr-17<br>
Shot to death</p>
<p>Sufaid<br>
Nowshera, Pakistan<br>
14-Aug-17<br>
Shot to death</p>
<p>Chanda Sharmeeli<br>
Karachi, Pakistan<br>
30-Aug-17<br>
Shot to death</p>
<p><strong>Paraguay</strong></p>
<hr>
<p>Name unknown<br>
Ciudad del Este, Paraguay<br>
6-Dec-16<br>
Shot</p>
<p><strong>Philippines</strong></p>
<hr>
<p>Heart De Chavez<br>
Metro Manilla, Philippines<br>
10-Jan-17<br>
Shot</p>
<p>J. R. P. Mangalili<br>
Bulacan, Philippines<br>
6-Feb-17<br>
Deliberately ran over by a vehicle</p>
<p>Name unknown<br>
Philippines<br>
13-Feb-17<br>
Beaten</p>
<p>Charlotte Oquias Lapasaran Logronio<br>
Davao, Philippines<br>
22-Feb-17<br>
Shot</p>
<p>Jheayn<br>
Metro Manilla, Philippines<br>
10-Apr-17<br>
Beaten</p>
<p>J. R. P. Mangalili<br>
Bulacan, Philippines<br>
2-Jun-17<br>
Deliberately struck by vehicle</p>
<p><strong>Russia</strong></p>
<hr>
<p>Name unknown<br>
Voronezh, Russia<br>
19-Jan-17<br>
Beaten and strangled to death, after which her apartment was set on fire</p>
<p><strong>Saudi Arabia</strong></p>
<hr>
<p>Amna<br>
Riyadh, Saudi Arabia<br>
1-Feb-17<br>
Tortured to death by the police after chargers of “cross-dressing” and having “same-sex” relationships.</p>
<p>Meeno<br>
Riyadh, Saudi Arabia<br>
1-Feb-17<br>
Tortured to death by the police after chargers of “cross-dressing” and having “same-sex” relationships.</p>
<p><strong>South Africa</strong></p>
<hr>
<p>Sihle<br>
Eastern Cape, South Africa<br>
6-Aug-17<br>
Stabbed</p>
<p><strong>Sweden</strong></p>
<hr>
<p>Madeleine Delbom<br>
Borlänge, Sweden<br>
24-Nov-16<br>
Strangled and stabbed to death</p>
<p><strong>Thailand</strong></p>
<hr>
<p>Ying<br>
Nakorn Pathom, Thailand<br>
13-Dec-16<br>
Suffocated</p>
<p>Puriwit Chanasit (Keng)<br>
Hatyai Songkla, Thailand<br>
6-Jan-17<br>
Murdered</p>
<p>Nampuang<br>
Pranaknrnsri Ayuthaya, Thailand<br>
12-Feb-17<br>
Stabbed</p>
<p>P. J.<br>
Doi Saket, Chiang Mai, Thailand<br>
2-Mar-17<br>
Stabbed</p>
<p>Rapee<br>
Kantharalak, Srisaket, Thailand<br>
14-Mar-17<br>
Beaten</p>
<p><strong>United States of America</strong></p>
<hr>
<p>India Monroe, aka India Thedarkvixen<br>
Newport News, Virginia, USA<br>
21-Dec-16<br>
Multiple gunshot wounds.</p>
<p>Mesha Caldwell<br>
Canton, Mississippi, USA<br>
4-Jan-17<br>
Shot to death</p>
<p>Jamie Lee Wounded Arrow<br>
Sioux Falls, South Dakota, USA<br>
7-Jan-17<br>
Undetermined</p>
<p>Jojo Striker<br>
Toledo, Ohio, USA<br>
8-Feb-17<br>
Shot to death</p>
<p>Jaquarrius Holland<br>
Monroe, Louisiana, USA<br>
19-Feb-17<br>
Shot</p>
<p>Tiara Richmond aka Keke Collier<br>
Chicago, Illinois, USA<br>
21-Feb-17<br>
Shot</p>
<p>Chyna Gibson, aka Chyna Doll Dupree<br>
New Orleans, Louisiana, USA<br>
25-Feb-17<br>
Shot to death</p>
<p>Ciara McElveen<br>
New Orleans, Louisiana, USA<br>
27-Feb-17<br>
Multiple stab wounds.</p>
<p>Alphonza Watson<br>
Baltimore, Maryland, USA<br>
22-Mar-17<br>
Shot to death</p>
<p>Kenne McFadden<br>
San Antonio, Texas, USA<br>
9-Apr-17<br>
Drowned</p>
<p>Chay “Juicy” Reed<br>
Miami, Florida, USA<br>
21-Apr-17<br>
Shot to death</p>
<p>Mx. Bostick<br>
New York, New York, USA<br>
4-May-17<br>
Attacked with a metal pipe on the 24th of April.<br>
<em>Note:</em> There has been a lot of confusion as to the gender identity of this individual. What we do know is that they were born male, and that they did for a period of time live as a female. At the time of their death, they were homeless and presenting as male. As such, we have put a gender neutral designator on this name, and are using they/them pronouns. As with every case presented, any additional information would be desired.</p>
<p>Sherrell Faulkner<br>
Charlotte, North Carolina, USA<br>
16-May-17<br>
Passed away from injuries sustained in a November 30th, 2016 attack</p>
<p>Imer Alvarado<br>
Fresno, CA<br>
17-May-17<br>
Shot<br>
<em>Note:</em> Alvarado did not identify as a transgender woman, but as a gay male. He was, nevertheless, presenting in female attire at the time of his murder, and this may have had a part in this death.</p>
<p>Kendra Adams, aka Josie Berrios and Kimbella Rosé<br>
Ithaca, New York, USA<br>
13-Jun-17<br>
Murdered and burnt</p>
<p>Ebony Morgan<br>
Lynchburg, Virginia, USA<br>
2-Jul-17<br>
Multiple gunshot wounds</p>
<p>TeeTee Dangerfield<br>
College Park, Georgia, USA<br>
1-Aug-17<br>
Multiple gunshot wounds.</p>
<p>Gwynevere River Song<br>
Waxahachie, Texas, USA<br>
12-Aug-17<br>
Shot</p>
<p>Kiwi Herring<br>
Saint Louis, Missouri, USA<br>
22-Aug-17<br>
Shot by police in suspicious circumstances<br>
<em>Note:</em> While Herring was killed by the St. Louis Police Department, allegedly while brandishing a knife at officers, there were circumstances surrounding this death that were anti-transgender in nature, including threats and actions from a neighbor that led to the confrontation that led to Herring’s death.</p>
<p>Anthony “Bubbles” Torres<br>
San Francisco, California, USA<br>
9-Sep-17<br>
Shot<br>
<em>Note:</em> Like Imer Alvarado, above, Bubbles did not identify as a transgender woman. He was, nevertheless, presenting in feminine attire at the time of his murder, and this may have had a hand in this death.</p>
<p>Derricka Banner<br>
Charlotte, North Carolina, USA<br>
12-Sep-17<br>
Shot to death</p>
<p>Ally Lee Steinfeld<br>
Licking, Missouri, USA<br>
21-Sep-17<br>
Ally was stabbed, including wounds to the genitals. Her eyes were also gouged out. Her body was burned in an attempt to conceal evidence of the crime, and some of Ally’s bones were put into a garbage bag placed in a chicken coop near the residence.</p>
<p>Stephanie Montez<br>
Robstown, Texas, USA<br>
26-Oct-17<br>
Multiple gunshot wounds</p>
<p>Candace Towns.<br>
Macon, Georgia, USA<br>
31-Oct-17<br>
Shot to death</p>
<p><strong>Venezuela</strong></p>
<hr>
<p>Alexandra Peña Vizcaya<br>
Chiquinquira, Venezuela<br>
12-Feb-17<br>
Multiple gunshot</p>
<p>Name unknown<br>
Barquisimeto, Venezuela<br>
28-Feb-17<br>
Shot multiple times</p>
<p>Alejandra Diaz<br>
Baruta, Venezuela<br>
25-May-17<br>
Shot</p>
<p>Name unknown<br>
Venezuela, Venezuela<br>
29-Jul-17<br>
Not reported</p>
<p>Name unknown<br>
Chiquinquira, Venezuela<br>
20-Aug-17<br>
Beaten and stabbed</p>
"""
import re
import googlemaps

from googlemaps.exceptions import TransportError
gmaps = googlemaps.Client(key='AIzaSyCyMnYYcoEGCLeu5ghxvqlUbluo2PUC1hk')

def geocode_google(city, country):
    """
    Geocode against Google
    Return point as array of [lat, lng] if geocoded, None otherwise.
    """
    try:
        address_submission = "{} {}".format(city.strip(), country.strip())
        
        geocode_results = gmaps.geocode(address = address_submission)

        if len(geocode_results):
            return geocode_results[0]['geometry']['location']
        else:
            return None
    except TransportError as e:
        print("Google geocoding error: {}".format(e))
        return None


inputArray = input.split("\n")
currentCountry = ""
currentName = ""
currentCity = ""
currentDate = ""
currentCause = ""

people = []

for row in inputArray:
##    print(row)
    countrySearch = re.search(u"<p><strong>(.*)</strong></p>", row)
    nameSearch = re.search(u"<p>(.*)<br>", row)
    dateSearch = re.search(u"([0-9]{1,2}-[a-zA-Z]*-[0-9]{2})<br>", row)
    cityDateSearch = re.search(u"(.*)<br>", row) # will match cities AND dates
    causeSearch = re.search(u"(.*)</p>", row)
    if countrySearch:
        currentCountry = countrySearch.group(1)
##        print(currentCountry)
    elif nameSearch:
        coordinates = geocode_google(currentCity, currentCountry)
        if coordinates:
            people.append(
                {
                  'type': 'Feature',
                  'geometry': {
                    'type': 'Point',
                    'coordinates': [coordinates['lng'], coordinates['lat']],
                  },
                          'properties': {
                                'name': currentName,
                                'city': currentCity,
                                'date': currentDate,
                                'cause': currentCause,
                  }
                  }
                )
        
        currentName = nameSearch.group(1)
##        print(currentName)
    elif dateSearch:
        currentDate = dateSearch.group(1)
##        print(currentDate)
    elif cityDateSearch:
        currentCity = cityDateSearch.group(1)
##        print(currentCity)
    elif causeSearch:
        currentCause = causeSearch.group(1)
##        print(currentCause)

print(people)
