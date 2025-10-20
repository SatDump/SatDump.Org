import json

statuses = {
    "a": "🟢 ",  # Active
    "i": "🔴 ",  # Inoperational (permanently off)
    "d": "🔵 ",  # Disabled (operational but off)
    "u": "🟡 ",  # Unknown
}


class SampleData:
    """A sample image with hotlink and credit"""

    def __init__(self, name: str, url: str):
        self.name = name
        self.url = url

    def __repr__(self):
        return self.name + " - " + self.url


class Signal:
    """A satellite signal"""

    def __init__(
        self,
        name: str,
        status: str,
        frequency: str,
        polarization: str,
        symbolrate: str,
        image: str,
        description: str,
        data: list[SampleData],
    ):
        self.name = name
        self.status = status  # a = active, u = unknown, f = failed, i = inop
        self.frequency = frequency
        self.polarization = polarization
        self.symbolrate = symbolrate
        self.image = image
        self.description = description

        self.data: list[SampleData] = []

        for sample_data in data:
            if isinstance(sample_data, SampleData):
                self.data.append(sample_data)

            else:
                self.data.append(SampleData(**sample_data))

    def to_JSON(self):
        """Returns object as JSON compliant dict

        Returns:
            str: self as JSON dict
        """
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)

    def __repr__(self):
        """Allows nicer printing for debug purposes

        Returns:
            str: A formatted print
        """
        out = f"{self.name} -> {self.frequency} {self.polarization} {self.symbolrate} \n\n>Image URL: {self.image}\n>Description:\n{self.description}\n\n"

        out += ">Sample data:\n"
        for image in self.data:
            out += f"    - {image.name} - {image.url}\n"

        return out


class Satellite:
    """Satellite object"""

    def __init__(
        self,
        name: str,
        norad: int,
        agency: str,
        start: str,
        end: str,
        description: str,
        signals: list[Signal],
    ):
        self.name = name
        self.norad = norad
        self.agency = agency
        self.start = start
        self.end = end
        self.description = description
        self.signals: list[Signal] = []

        for signal in signals:
            if isinstance(signal, Signal):
                self.signals.append(signal)

            else:
                self.signals.append(Signal(**signal))

    def to_JSON(self) -> str:
        """Returns object as JSON compliant dict

        Returns:
            str: self as JSON dict
        """
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=False, indent=4)

    def __repr__(self):
        """Allows nicer printing for debug purposes

        Returns:
            str: A formatted print
        """
        out = f"{self.name} [NORAD {self.norad}] \n{self.start} - {self.end}\nAgency: {self.agency}\nDescription:\n"

        out += self.description

        out += "\n\nSignals:\n"

        for signal in self.signals:
            out += f"--> {signal}"

        return out

    def to_markdown(self) -> str:
        """Converts the class to a markdown compliant format (with some html elements)

        Returns:
            str: Formatted MD
        """

        def add_column(item: str) -> str:
            """Returns a html table column

            Args:
                item (str): Contents of coumn

            Returns:
                str: <td>Item</td>
            """
            return "<td>" + item + "</td>"

        # Title
        out = f"# {self.name} [NORAD [{self.norad}](https://www.n2yo.com/satellite/?s={self.norad})]\n"

        # Sat footer text
        if self.end:
            out += f"<small>*{self.start} - {self.end} | Agency: {self.agency}*</small>\n\n"
        else:
            out += f"<small>*{self.start} • Agency: {self.agency}*</small>\n\n"

        out += self.description

        # Signals
        out += "<br>\n<b>Transmitted signals:\n\n"

        out += "<table>\n"
        out += "<tr><th>Name</th><th>FFT image</th><th>Frequency</th><th>Polarization,<br>Symbol rate</th><th>Sample data</th></tr>\n"

        for signal in self.signals:

            # No borders so description is merged to it
            out += '<tr style="border-top: none; border-bottom: none; border-left: none; border-right: none;">'

            # Name column
            out += add_column(f"<b>{statuses[signal.status]}{signal.name}</b>")

            # FFT image column
            if signal.image:
                out += add_column(
                    f"<img src='/assets/sat-list/fft/{signal.image}' alt='{signal.name} FFT image'>"
                )
            else:
                out += add_column("-")

            # Signal frequency column
            out += add_column(signal.frequency)

            # Polarization + symbol rate column
            out += f"<td>{signal.polarization}<br>"
            if signal.symbolrate:
                out += signal.symbolrate
            else:
                out += "??? sym/s"
            out += "</td>"

            # Sample data column
            if signal.data:
                out += '<td style="line-height: 1;">'
                out += "<br>".join(
                    f"<a href='{data.url}'>{data.name}</a> <br>"
                    for data in signal.data
                )
                out += "</td>"
            else:
                out += add_column("-")

            out += "</tr>\n"

            # Signal description is placed below every signal
            out += "<tr>"
            out += '<td style= "text-align: left; white-space: normal; word-wrap: break-word; overflow-wrap: break-word;" colspan="5" >'
            if not signal.description:
                out += "-"
            out += f"{signal.description}"
            out += "</td>"
            out += "</tr>\n"

        out += "</table>\n"

        return out
