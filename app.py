from flask import Flask, jsonify, request
import matplotlib.pyplot as plt
import io
import base64
from flask_cors import CORS

import matplotlib
matplotlib.use('Agg')  # Agg arka planını kullan

app = Flask(__name__)
CORS(app)

def create_pie_chart(sizes, labels, colors):
    # Grafik boyutunu ve stilini ayarla
    plt.figure(figsize=(8,6))
    plt.style.use('dark_background')
    
    # 'Doughnut' pie chart oluştur
    wedges, texts, autotexts = plt.pie(sizes, labels=labels, colors=colors, autopct='%1.2f%%', startangle=140, pctdistance=0.85)

    # Orta kısmı boşaltarak 'doughnut' görünümü kazandır
    centre_circle = plt.Circle((0,0),0.70,fc='white')
    fig = plt.gcf()
    fig.gca().add_artist(centre_circle)

    # Autotext'leri özelleştir
    plt.setp(autotexts, size=8, weight="bold", color="white")

    # Başlık ekle
    plt.title('Total assets allocation', color='white', fontsize=14)

    # Legend'i özelleştir
    plt.legend(loc='upper left', fontsize=10)

    # Eksen eşitliğini sağla
    plt.axis('equal')

    # Grafik görselini kaydet
    img = io.BytesIO()
    plt.savefig(img, format='png', bbox_inches='tight', transparent=True)
    img.seek(0)
    plt.close()

    return base64.b64encode(img.getvalue()).decode()


def create_line_chart(x_values, y_values):
    plt.figure(figsize=(10,6))
    plt.plot(x_values, y_values, marker='o')
    plt.title('Örnek Line Chart')
    plt.xlabel('X Ekseni')
    plt.ylabel('Y Ekseni')

    img = io.BytesIO()
    plt.savefig(img, format='png', bbox_inches='tight')
    img.seek(0)
    plt.close()
    return base64.b64encode(img.getvalue()).decode()

@app.route('/piechart', methods=['POST'])
def piechart():
    data = request.json
    sizes = data['sizes']
    labels = data['labels']
    image = create_pie_chart(sizes, labels,colors=['red','blue','green'])
    return jsonify({'image': image})

@app.route('/linechart', methods=['POST'])
def linechart():
    data = request.json
    x_values = data['x_values']
    y_values = data['y_values']
    image = create_line_chart(x_values, y_values)
    return jsonify({'image': image})
@app.route('/custompiechart', methods=['POST'])
def custom_piechart():
    data = request.json
    sizes = data['sizes']
    labels = data['labels']
    colors = data['colors']  # Renkler listesi de gönderilmeli
    image = create_pie_chart(sizes, labels, colors)
    return jsonify({'image': image})
def create_interactive_line_chart(x_values, y_values):
    # Plotly çizgi grafiği oluştur
    fig = go.Figure(data=go.Scatter(x=x_values, y=y_values, mode='lines+markers'))
    
    # Etkileşimli grafik özelliklerini ayarla
    fig.update_layout(
        title='Etkileşimli Line Chart',
        xaxis_title='X Ekseni',
        yaxis_title='Y Ekseni',
        margin={'l': 40, 'b': 40, 't': 40, 'r': 40},
        hovermode='closest'
    )
    
    # Zoom ve pan özelliklerini etkinleştir
    fig.update_xaxes(showgrid=False, zeroline=False, rangeslider_visible=True)
    fig.update_yaxes(showgrid=False, zeroline=False)
    
    # Plotly grafiğini JSON formatında döndür
    graphJSON = json.dumps(fig, cls=PlotlyJSONEncoder)
    return graphJSON

@app.route('/interactive-linechart', methods=['POST'])
def interactive_linechart():
    data = request.json
    x_values = data['x_values']
    y_values = data['y_values']
    graphJSON = create_interactive_line_chart(x_values, y_values)
    return jsonify(graphJSON)

if __name__ == '__main__':
    app.run(debug=True)

if __name__ == '__main__':
    app.run(debug=True)
