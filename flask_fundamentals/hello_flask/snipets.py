<table>
        {% for i in range(4): %}
        <tr>
            {% for j in range(8): %}
            <td class='color1'></td>
            <td class='color2'></td>
            {% endfor %}
        </tr>
        <tr>
            {% for j in range()%}
            <td class='color2'></td>
            <td class='color1'></td>
            {% endfor %}
        </tr>
        {% endfor %}
    </table>